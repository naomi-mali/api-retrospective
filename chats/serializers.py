from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Chat, Message


class ChatSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')
    sender_image = serializers.ReadOnlyField(source='sender.profile.image.url')
    receiver_username = serializers.ReadOnlyField(source='receiver.username')
    receiver_image = serializers.ReadOnlyField(source='receiver.profile.image.url')
    last_message = serializers.SerializerMethodField()
    unread_message_count = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    def get_last_message(self, obj):
        last_message = obj.messages.order_by('-created_at').first()
        return last_message.message if last_message else None

    def get_unread_message_count(self, obj):
        user = self.context['request'].user
        message_count = obj.messages.filter(
            chat=obj, chat__sender=user, seen=False).count()
        return message_count

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    class Meta:
        model = Chat
        fields = [
            'id',
            'sender',
            'sender_image',
            'receiver',
            'receiver_username',
            'receiver_image',
            'created_at',
            'last_message',
            'unread_message_count',
            'message',
        ]


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')
    receiver = serializers.ReadOnlyField(source='get_receiver_username')
    created_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def validate_message(self, value):
        if not value.strip():
            raise serializers.ValidationError("Message cannot be empty.")
        return value

    class Meta:
        model = Message
        fields = [
            'id',
            'sender',
            'message',
            'receiver',
            'created_at',
            'seen',
        ]
        read_only_fields = ['seen']
