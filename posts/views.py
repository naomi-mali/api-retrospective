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
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',]
        
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

class ReportCreateView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = ReportSerializer(data=data)

        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
