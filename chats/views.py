from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError, PermissionDenied
from api_retrospective.permissions import IsSenderOrReceiver, IsChatSender
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated


class ChatList(generics.ListCreateAPIView):
    """
    List all chats or create a new chat instance.
    """
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated, IsSenderOrReceiver]

    def get_queryset(self):
        user = self.request.user
        return Chat.objects.filter(sender=user) | Chat.objects.filter(receiver=user)

    def perform_create(self, serializer):
        sender = self.request.user
        receiver = serializer.validated_data['receiver']
        
        if Chat.objects.filter(sender=sender, receiver=receiver).exists() or \
           Chat.objects.filter(sender=receiver, receiver=sender).exists():
            raise ValidationError({'detail': 'Chat with this user already exists.'})
        elif sender == receiver:
            raise ValidationError({'detail': 'You cannot send a message to yourself.'})

        serializer.save(sender=sender, receiver=receiver)


class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a chat instance.
    """
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated, IsSenderOrReceiver, IsChatSender]

    def get_queryset(self):
        user = self.request.user
        return Chat.objects.filter(sender=user) | Chat.objects.filter(receiver=user)


class MessageList(generics.ListCreateAPIView):
    """
    List all messages or create a new message instance within a chat.
    """
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated, IsSenderOrReceiver]

    def get_queryset(self):
        user = self.request.user
        chat_id = self.kwargs['pk']
        
        try:
            chat = Chat.objects.get(id=chat_id)
            if chat.sender == user or chat.receiver == user:
                return chat.messages.all()
            else:
                raise PermissionDenied({'detail': 'You cannot access this chat.'})
        except Chat.DoesNotExist:
            raise ValidationError({'detail': 'Chat does not exist.'})

    def perform_create(self, serializer):
        chat_id = self.kwargs['pk']
        user = self.request.user
        
        try:
            chat = Chat.objects.get(id=chat_id)
            if chat.sender == user or chat.receiver == user:
                serializer.save(chat=chat, sender=user)
            else:
                raise PermissionDenied({'detail': 'You cannot access this chat.'})
        except Chat.DoesNotExist:
            raise ValidationError({'detail': 'Chat does not exist.'})


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific message within a chat.
    """
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated, IsSenderOrReceiver]

    def get_object(self):
        user = self.request.user
        chat_id = self.kwargs['pk']
        message_id = self.kwargs['message_pk']

        try:
            chat = Chat.objects.get(pk=chat_id)
            if chat.sender != user and chat.receiver != user:
                raise PermissionDenied({'detail': 'You cannot access this chat.'})

            message = chat.messages.get(pk=message_id)
            return message

        except Chat.DoesNotExist:
            raise ValidationError({'detail': 'Chat does not exist.'})
        except Message.DoesNotExist:
            raise ValidationError({'detail': 'Message does not exist.'})

    def perform_update(self, serializer):
        user = self.request.user
        message = self.get_object()

        if message.sender == user:
            # The sender is allowed to update their message without changing the seen status.
            serializer.save(seen=False)
        elif message.chat.receiver == user:
            # Only the receiver can mark the message as seen, not edit it.
            if 'message' in serializer.validated_data:
                raise ValidationError({'detail': 'You cannot edit the message you received.'})
            message.seen = True
            message.save()
