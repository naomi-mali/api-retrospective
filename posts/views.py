from django.db.models import Count
from rest_framework import viewsets, generics, permissions, status, filters
from django_filters.rest_framework import DjangoFilterBackend
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
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    Retrieve a post and edit, delete, or report it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')

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
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        """
        Handle post requests to report a post.
        """
        post_id = request.data.get('post')
        if not post_id:
            return Response({'detail': 'Post ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        post = Post.objects.filter(id=post_id).first()
        if not post:
            return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

    
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
