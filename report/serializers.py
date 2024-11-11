from rest_framework import serializers
from .models import Report



class ReportSerializer(serializers.ModelSerializer):
    """Report serializer to convert Report model to JSON"""

    class Meta:
        """Meta field to specify the model and fields"""
        model = Report
        fields = ['post', 'user', 'comment', 'category', 'created_at']