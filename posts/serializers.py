from rest_framework import serializers
from posts.models import Post, Report
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    tagged_users = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username', many=True, required=False, allow_null=True
    )
    
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

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'created_at', 'updated_at', 'title', 'description',
            'image', 'category', 'tagged_users', 'location',
        ]


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['post', 'user', 'reason', 'category']
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)  

