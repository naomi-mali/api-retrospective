from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from report.models import Report
from django.contrib.auth.models import User
from posts.models import Post

class ReportListViewTests(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='password')

        # Create a Post to be used for testing
        self.post = Post.objects.create(title="Test Post", description="This is a test post.", category="ValidCategory", owner=self.user)
        
        # URL for ReportList view
        self.url = reverse('report-list')

    def test_user_can_create_report_with_post(self):
        """Test that the user can create a report with a post"""
        data = {
            'post': self.post.id,  # Use the created post ID
            'category': 'Spam',     # Example valid category
            'comment': 'Inappropriate content!'
        }
        self.client.login(username='testuser', password='password')
        response = self.client.post(self.url, data, format='json')

        # Check if report is created and response is correct
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Report.objects.count(), 1)
        self.assertEqual(Report.objects.first().post, self.post)

    def test_user_cannot_create_report_without_post(self):
        """Test that the user cannot create a report without a post"""
        data = {
            'category': 'Spam',   # Missing 'post' field
            'comment': 'This is a test report.'
        }
        self.client.login(username='testuser', password='password')
        response = self.client.post(self.url, data, format='json')
        
        # Check for bad request due to missing 'post' field
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Check that the 'post' field is included in the response errors
        self.assertIn('post', response.data)
        self.assertIn('This field is required', str(response.data['post'][0]))  # Ensure correct error message

    def test_user_cannot_create_report_with_invalid_category(self):
        """Test that the user cannot create a report with an invalid category"""
        data = {
            'post': self.post.id,  # Valid post
            'category': 'InvalidCategory',  # Invalid category
            'comment': 'Inappropriate content!'
        }
        self.client.login(username='testuser', password='password')
        response = self.client.post(self.url, data, format='json')

        # Check for bad request due to invalid category
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('category', response.data)
        self.assertIn('is not a valid choice', str(response.data['category'][0]))  # Check for invalid category error

    def test_user_can_list_reports(self):
        """Test that the user can list reports"""
        # Create two reports for listing
        Report.objects.create(post=self.post, category='Spam', comment='Inappropriate content!', user=self.user)
        Report.objects.create(post=self.post, category='Abuse', comment='Offensive content!', user=self.user)

        self.client.login(username='testuser', password='password')
        response = self.client.get(self.url, format='json')

        # Check if the reports are returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Ensure 2 reports are returned
