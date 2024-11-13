from rest_framework import generics, filters
from .models import Report
from .serializers import ReportSerializer


class ReportList(generics.ListCreateAPIView):
    """Allows users to submit Report and view a list of reports."""
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = []

    def perform_create(self, serializer):
        # Associate the report with the current user
        serializer.save(user=self.request.user)

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,  # You can also add ordering if needed
    ]

    # Exact match filtering for specific fields
    filterset_fields = ['user', 'category']

    # Fields that are searchable with full-text search
    search_fields = ['user__username', 'category', 'comment', 'title']

    # Optionally, allow sorting by fields like created_at
    ordering_fields = ['created_at', 'category']
    ordering = ['-created_at']  # Default ordering