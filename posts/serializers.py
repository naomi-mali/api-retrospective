from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from comments.models import Comment


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        """
        Validates that the image is not larger than 2MB,
        higher than 4096px and wider than 4096px.
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError('Image height larger than 4096px!')
        if value.image.width > 4096:
            raise serializers.ValidationError('Image width larger than 4096px!')
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    def to_representation(self, instance):
        """
        Overrides the default to_representation to add dynamically calculated fields.
        """
        # Prefetch related data for likes and comments
        self.context['request'].user = instance.owner
        representation = super().to_representation(instance)
        
        # Calculates likes_count and comments_count dynamically if not already present
        representation['likes_count'] = Like.objects.filter(post=instance).count()
        representation['comments_count'] = Comment.objects.filter(post=instance).count()

        return representation

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'created_at', 'updated_at', 'title', 'description',
            'image', 'category', 'like_id',  'location',
            'likes_count', 'comments_count',
        ]
