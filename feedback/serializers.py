from rest_framework import serializers
from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    """Feedback serializer to convert Feedback model to JSON"""

    class Meta:
        """Meta field to specify the model and fields"""
        model = Feedback
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'content',
            'created_at'
        ]