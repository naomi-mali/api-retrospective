from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.
    Adds additional fields for owner details and formatted timestamps.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """Checks if the current user is the owner of the comment."""
        request = self.context.get('request')
        return request and request.user == obj.owner

    def get_created_at(self, obj):
        """Returns the human-readable version of the creation timestamp."""
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """Returns the human-readable version of the update timestamp."""
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'post', 'created_at', 'updated_at', 'content',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in detail views.
    The `post` field is read-only to avoid setting it on updates.
    """
    post = serializers.ReadOnlyField(source='post.id')
