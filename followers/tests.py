from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from followers.models import Follower


class FollowersCreateDetailViewTest(APITestCase):
    def setUp(self):
        """
        Set up the tests by creating 2 users
        """
        test_user1 = User.objects.create_user(
            username='testuser1',
            password='testpassword'
        )
        test_user2 = User.objects.create_user(
            username='testuser2',
            password='testpassword'
        )
        test_user3 = User.objects.create_user(
            username='testuser3',
            password='testpassword'
        )
        Follower.objects.create(
            owner=test_user1,
            followed_id=3
        )

    def test_non_logged_in_user_cannot_follow(self):
        """
        Test that a non logged in user cannot follow a user
        """
        response = self.client.post('/followers/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_in_user_can_follow_a_user(self):
        """
        Test that a logged in user can follow another user
        """
        self.client.login(username='testuser1', password='testpassword')
        response = self.client.post('/followers/', {'followed': 2})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        follower_count = Follower.objects.all().count()
        self.assertEqual(follower_count, 2)

    def test_user_can_unfollow_a_user(self):
        """
        Test that a user can un-follow another user
        """
        self.client.login(username='testuser1', password='testpassword')
        response = self.client.delete('/followers/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        follower_count = Follower.objects.all().count()
        self.assertEqual(follower_count, 0)