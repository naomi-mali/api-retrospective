# views.py
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Post
from .serializers import PostSerializer
from api_retrospective.permissions import IsOwnerOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Post instances.
    Allows authenticated users to create, read, update, and delete posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [ IsOwnerOrReadOnly] 

    def perform_create(self, serializer):
        """
        Override the perform_create method to associate the post
        with the current authenticated user.
        """
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        """
        Override the perform_update method to customize the update behavior.
        Here, you can add additional logic if needed.
        """
        serializer.save()

    def perform_destroy(self, instance):
        """
        Override the perform_destroy method if you want to customize
        the delete behavior.
        """
        instance.delete()

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

class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        # Save the post with the current user as the owner
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()

    def perform_update(self, serializer):
        # Handle tagged users during update if applicable
        tagged_users = self.request.data.get('tagged_users')
        if tagged_users is not None and tagged_users == []:
            serializer.save(tagged_users=[])
        else:
            serializer.save()

