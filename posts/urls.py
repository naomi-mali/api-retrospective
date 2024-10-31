# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostList, PostDetail, UserAutocomplete, ReportPostView



urlpatterns = [
    
    # Direct URLs for the list, detail, and autocomplete views
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('user-autocomplete/', UserAutocomplete.as_view(), name='user-autocomplete'),
    path('posts/report/', ReportPostView.as_view(), name='report-post'),
]
