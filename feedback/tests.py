from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Feedback


class FeedbackListTest(APITestCase):
    def setUp(self):
        """
        Set up the test by creating a user and feedback instance.
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.feedback = Feedback.objects.create(
            first_name='test',
            last_name='user',
            email='name@example.com',
            content='test content'
        )

    def test_non_logged_in_user_can_submit_feedback(self):
        """
        Test that a non-logged-in user can submit feedback
        """
        response = self.client.post('/feedback/', {
            'first_name': 'test',
            'last_name': 'user',
            'email': 'name@example.com',
            'content': 'test content'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_in_user_can_submit_feedback(self):
        """
        Test that a logged-in user can submit feedback
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/feedback/', {
            'first_name': 'test',
            'last_name': 'user',
            'email': 'name@example.com',
            'content': 'test content'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_cannot_submit_feedback_without_content(self):
        """
        Test that a user cannot submit feedback without content
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/feedback/', {
            'first_name': 'test',
            'last_name': 'user',
            'email': 'name@example.com',
            'content': ''
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_cannot_submit_feedback_without_email(self):
        """
        Test that a user cannot submit feedback without an email
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/feedback/', {
            'first_name': 'test',
            'last_name': 'user',
            'email': '',
            'content': 'test content'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_can_view_feedback(self):
        """
        Test that a user can view feedback
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/feedback/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_feedback_submission_fields_are_required(self):
        """
        Test that missing required fields (e.g., first_name, last_name) return a 400 error.
        """
        response = self.client.post('/feedback/', {
            'first_name': '',
            'last_name': 'user',
            'email': 'name@example.com',
            'content': 'test content'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post('/feedback/', {
            'first_name': 'test',
            'last_name': '',
            'email': 'name@example.com',
            'content': 'test content'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
