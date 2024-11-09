from django.db.models import Count
from rest_framework import viewsets, generics, permissions, status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Post, Report
from .serializers import PostSerializer, ReportSerializer
from api_retrospective.permissions import IsOwnerOrReadOnly



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
        'owner__username',
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

class MentionsList(APIView):
    """
    Provides a list of user mentions based on a search query.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  

    def get(self, request):
        search_query = request.query_params.get('search', '').strip()  
        if search_query:
            users = User.objects.filter(username__icontains=search_query)[:10] 
        else:
            users = User.objects.all()[:10] 
        mentions = [{"id": str(user.id), "name": user.username} for user in users]
        return Response(mentions)       


class ReportPostView(generics.RetrieveUpdateAPIView):
    """
    View for reporting a post. Allows creating or updating a report.
    """
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Report.objects.all()

    def perform_create(self, serializer):
        # Create a new report
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        # Update an existing report
        serializer.save()

    def get_object(self):
        """
        Retrieve the existing report if it exists, otherwise return None.
        """
        post_id = self.kwargs.get('post_id')
        report = Report.objects.filter(post_id=post_id, user=self.request.user).first()
        if report:
            return report
        return None

    def post(self, request, *args, **kwargs):
        """
        Handle POST request to report a post (create a new report).
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

    def put(self, request, *args, **kwargs):
        """
        Handle PUT requests to update a report.
        """
        post_id = request.data.get('post')
        if not post_id:
            return Response({'detail': 'Post ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        post = Post.objects.filter(id=post_id).first()
        if not post:
            return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the report exists
        report = Report.objects.filter(post=post, user=request.user).first()
        if not report:
            return Response({'detail': 'You have not reported this post yet.'}, status=status.HTTP_400_BAD_REQUEST)

        # Update the report
        report.reason = request.data.get('reason', report.reason)
        report.category = request.data.get('category', report.category)
        report.save()

        return Response({'detail': 'Report updated successfully.'}, status=status.HTTP_200_OK)


class ReportListView(generics.ListAPIView):
    """
    View to list all reports.
    """
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned reports to a given user,
        by filtering against a `user` query parameter in the URL.
        """
        queryset = Report.objects.all() 
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)  
        return queryset

    def list(self, request, *args, **kwargs):
        """
        Handle GET requests to fetch the list of reports.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)