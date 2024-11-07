# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostList, PostDetail, ReportPostView



urlpatterns = [
    
    # Direct URLs for the list, detail, and autocomplete views
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('posts/report/', ReportPostView.as_view(), name='report-post'),
]
