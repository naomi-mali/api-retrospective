from django.urls import path
from .views import ChatList, ChatDetail, MessageList, MessageDetail

urlpatterns = [
    path('chats/', ChatList.as_view(), name='chat-list'),  # For listing and creating chats
    path('chats/<int:pk>/', ChatDetail.as_view(), name='chat-detail'),  # For retrieving, updating, and deleting a chat
    path('chats/<int:pk>/messages/', MessageList.as_view(), name='message-list'),  # For listing and creating messages in a chat
    path('chats/<int:pk>/messages/<int:message_pk>/', MessageDetail.as_view(), name='message-detail'),  # For retrieving, updating, and deleting a message
]
