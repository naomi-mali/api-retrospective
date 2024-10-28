# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, PostList, PostDetail, UserAutocomplete

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    # Include the router URLs
    path('', include(router.urls)),
    
    # Direct URLs for the list, detail, and autocomplete views
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('user-autocomplete/', UserAutocomplete.as_view(), name='user-autocomplete'),  # Autocomplete URL
]
