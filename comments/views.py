from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from api_retrospective.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    View to list all comments or create a new comment if the user is logged in.
    - Supports filtering comments by the `post` field.
    - Requires authentication for creating a comment.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']  # Allows filtering by post ID.

    def perform_create(self, serializer):
        """
        Assign the currently authenticated user as the owner of the comment.
        """
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a specific comment by its ID.
    - Only the owner of the comment can update or delete it.
    - Read-only access is available to all authenticated or unauthenticated users.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
