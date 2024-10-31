# views.py
from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Post, Report
from .serializers import PostSerializer, ReportSerializer
from api_retrospective.permissions import IsOwnerOrReadOnly


class UserAutocomplete(APIView):
    """
    Returns a list of usernames that match the query parameter for autocomplete functionality.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        query = request.query_params.get('q', '')
        users = User.objects.filter(username__icontains=query)[:10]
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
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    Retrieve a post and edit, delete, or report it if you own it.
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


class ReportPostView(generics.CreateAPIView):
    """
    View for reporting a post.
    """
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically assign the current user to the report
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        """
        Handle post requests to report a post.
        """
        post_id = request.data.get('post')  # Retrieve post ID from the request data
        if not post_id:
            return Response({'detail': 'Post ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the post exists
        post = Post.objects.filter(id=post_id).first()
        if not post:
            return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Check if a report already exists for the post by the current user
        if Report.objects.filter(post=post, user=request.user).exists():
            return Response({'detail': 'You have already reported this post.'}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            'post': post.id,
            'reason': request.data.get('reason'),
            'category': request.data.get('category')
        }
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({'detail': 'Post reported successfully.'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
