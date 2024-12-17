from rest_framework import generics, filters
from .models import Feedback
from .serializers import FeedbackSerializer


class FeedbackList(generics.ListCreateAPIView):
    """Allows users to submit feedback."""
    
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = ['first_name', 'last_name', 'email', 'content']
