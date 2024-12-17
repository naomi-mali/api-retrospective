from rest_framework import generics, filters
from .models import Report
from .serializers import ReportSerializer


class ReportList(generics.ListCreateAPIView):
    """Allow users to submit reports and view a list of all reports."""

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = []

    def perform_create(self, serializer):
        """Associate the report with the current authenticated user."""
        serializer.save(user=self.request.user)

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ['user', 'category']

    search_fields = ['user__username', 'category', 'comment', 'title']

    ordering_fields = ['created_at', 'category']
    ordering = ['-created_at']
