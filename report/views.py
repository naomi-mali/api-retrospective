from rest_framework import generics, filters
from .models import Report
from .serializers import ReportSerializer


class ReportList(generics.ListCreateAPIView):
    """Allows users to submit Report"""
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = ['user', 'category', 'comment']