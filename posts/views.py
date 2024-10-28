from rest_framework import generics, permissions
from api_retrospective.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()

    def perform_update(self, serializer):
        tagged_users = self.request.data.get('tagged_users')
        if tagged_users is not None and tagged_users == []:
            serializer.save(tagged_users=[])
        else:
            serializer.save()


class UserAutocomplete(APIView):
    """
    Returns a list of usernames that match the query parameter for autocomplete functionality.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        query = request.query_params.get('q', '')  # Get the search query
        users = User.objects.filter(username__icontains=query)[:10]  # Limit results for performance
        usernames = [user.username for user in users]
        return Response(usernames)
