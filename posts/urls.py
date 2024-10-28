from django.urls import path, include
from .views import PostList, PostDetail, UserAutocomplete

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('user-autocomplete/', UserAutocomplete.as_view(), name='user-autocomplete'),  # Autocomplete URL
]
