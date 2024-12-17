from django.contrib.auth.models import User
from .models import Chat, Message
from rest_framework import status
from rest_framework.test import APITestCase


class ChatListViewTests(APITestCase):
    def setUp(self):
        self.adam = User.objects.create_user(username='adam', password='pass')
        self.brian = User.objects.create_user(username='brian', password='pass')

    def test_can_list_chats(self):
        """
        Test that a logged-in user can list their chats.
        """
        Chat.objects.create(sender=self.adam, receiver=self.brian)

        self.client.login(username='adam', password='pass')
        response = self.client.get('/chats/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_chat(self):
        """
        Test that a logged-in user can create a chat.
        """
        self.client.login(username='adam', password='pass')
        response = self.client.post('/chats/', {'receiver': self.brian.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Chat.objects.count(), 1)

    def test_user_not_logged_in_cant_create_chat(self):
        """
        Test that a non-logged-in user cannot create a chat.
        """
        response = self.client.post('/chats/', {'receiver': self.brian.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ChatDetailViewTests(APITestCase):
    def setUp(self):
        self.adam = User.objects.create_user(username='adam', password='pass')
        self.brian = User.objects.create_user(username='brian', password='pass')

    def test_can_retrieve_chat_using_valid_id(self):
        """
        Test that a user can retrieve a chat with a valid ID.
        """
        chat = Chat.objects.create(sender=self.adam, receiver=self.brian)

        self.client.login(username='adam', password='pass')
        response = self.client.get(f'/chats/{chat.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_chat_using_invalid_id(self):
        """
        Test that retrieving a chat with an invalid ID returns 404.
        """
        self.client.login(username='adam', password='pass')
        response = self.client.get('/chats/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_chat(self):
        """
        Test that a user can update their own chat.
        """
        chat = Chat.objects.create(sender=self.adam, receiver=self.brian)

        self.client.login(username='adam', password='pass')
        response = self.client.put(
            f'/chats/{chat.id}/', {'receiver': self.brian.id}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_chat(self):
        """
        Test that a user cannot update another user's chat.
        """
        chat = Chat.objects.create(sender=self.adam, receiver=self.brian)

        self.client.login(username='brian', password='pass')
        response = self.client.put(
            f'/chats/{chat.id}/', {'receiver': self.adam.id}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_chat(self):
        """
        Test that a user can delete their own chat.
        """
        chat = Chat.objects.create(sender=self.adam, receiver=self.brian)

        self.client.login(username='adam', password='pass')
        response = self.client.delete(f'/chats/{chat.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Chat.objects.count(), 0)

    def test_user_cant_delete_another_users_chat(self):
        """
        Test that a user cannot delete another user's chat.
        """
        chat = Chat.objects.create(sender=self.adam, receiver=self.brian)

        self.client.login(username='brian', password='pass')
        response = self.client.delete(f'/chats/{chat.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
