from rest_framework import serializers
from .models import Report



class ReportSerializer(serializers.ModelSerializer):
    """Report serializer to convert Report model to JSON"""

    class Meta:
        """Meta field to specify the model and fields"""
        model = Report
        fields = ['reason', 'category']

    def validate_category(self, value):
        if value not in dict(Report.CATEGORY_CHOICES).keys():
            raise serializers.ValidationError("Invalid category.")
        return value