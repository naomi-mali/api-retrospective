from rest_framework import serializers
from posts.models import Post, Report
from django.contrib.auth.models import User
from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    mentioned_users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    tagged_users = serializers.PrimaryKeyRelatedField(queryset=User .objects.all(), many=True, required=False)
    
    
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
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None    

    def create(self, validated_data):
        mentioned_users = validated_data.pop('mentioned_users', [])
        tagged_users = validated_data.pop('tagged_users', [])
        post = Post.objects.create(**validated_data)
        post.mentioned_users.set(mentioned_users)  # Set the many-to-many relationship
        post.tagged_users.set(tagged_users)  # Set the many-to-many relationship
        return post  
        
    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'created_at', 'updated_at', 'title', 'description',
            'image', 'category', 'like_id', 'tagged_users', 'mentioned_users', 'location',
            'likes_count', 'comments_count',
        ]


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['post', 'user', 'reason', 'category']
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)  

