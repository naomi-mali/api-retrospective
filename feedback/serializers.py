from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    """
    Serializer for the Feedback model.
    Converts Feedback model instances to JSON format and validates fields.
    """

    class Meta:
        model = Feedback
        fields = [
            'id',             # Primary key of the feedback instance
            'first_name',     # The first name of the user giving feedback
            'last_name',      # The last name of the user giving feedback
            'email',          # Email address of the user
            'content',        # The content of the feedback message
            'created_at'      # Timestamp of when the feedback was created
        ]
