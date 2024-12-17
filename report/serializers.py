from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    """Serializer for the Report model to convert it to JSON."""

    class Meta:
        """Meta class to define model and fields."""
        model = Report
        fields = ['title', 'user', 'category', 'comment', 'created_at']

    def validate_category(self, value):
        """Validate that the category is one of the predefined choices."""
        if value not in dict(Report.CATEGORY_CHOICES).keys():
            raise serializers.ValidationError("Invalid category.")
        return value
