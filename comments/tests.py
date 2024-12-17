from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Comment
from posts.models import Post


class CommentsCreateDetailViewTest(APITestCase):
    def setUp(self):
        """
        Set up the tests by creating users, posts, and comments.
        """
        self.test_user1 = User.objects.create_user(
            username='testuser1', password='testpassword'
        )
        self.test_user2 = User.objects.create_user(
            username='testuser2', password='testpassword'
        )
        self.post1 = Post.objects.create(
            owner=self.test_user1,
            title='Test Title 1',
            description='Test Description 1',
            category='family-and-friends',
        )
        self.post2 = Post.objects.create(
            owner=self.test_user2,
            title='Test Title 2',
            description='Test Description 2',
            category='family-and-friends',
        )
        self.comment1 = Comment.objects.create(
            owner=self.test_user1, post=self.post1, content='comment 1'
        )
        self.comment2 = Comment.objects.create(
            owner=self.test_user2, post=self.post2, content='comment 2'
        )

    def test_non_logged_in_user_cannot_create_a_comment(self):
        """
        Test that a non-logged-in user cannot create a comment.
        """
        response = self.client.post('/comments/', {
            'content': 'a comment',
            'post': self.post1.id
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_in_user_can_create_a_comment(self):
        """
        Test that a logged-in user can create a comment.
        """
        self.client.login(username='testuser1', password='testpassword')
        response = self.client.post('/comments/', {
            'post': self.post1.id,
            'content': 'a comment'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 3)

    def test_user_cannot_create_a_comment_with_no_content(self):
        """
        Test that a user cannot create a comment with no content.
        """
        self.client.login(username='testuser1', password='testpassword')
        response = self.client.post('/comments/', {
            'content': '',
            'post': self.post1.id
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_can_get_comment_by_id(self):
        """
        Test that a user can retrieve a comment by its ID.
        """
        self.client.login(username='testuser1', password='testpassword')
        response = self.client.get(f'/comments/{self.comment1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_get_comment_with_invalid_id(self):
        """
        Test that a user cannot retrieve a comment with an invalid ID.
        """
        self.client.login(username='testuser1', password='testpassword')
        response = self.client.get('/comments/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_their_own_comment(self):
        """
        Test that a user can update their own comment.
        """
        self.client.login(username='testuser1', password='testpassword')
        response = self.client.put(f'/comments/{self.comment1.id}/', {
            'content': 'updated comment'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.comment1.refresh_from_db()
        self.assertEqual(self.comment1.content, 'updated comment')

    def test_user_cannot_update_someone_elses_comment(self):
        """
        Test that a user cannot update someone else's comment.
        """
        self.client.login(username='testuser2', password='testpassword')
        response = self.client.put(f'/comments/{self.comment1.id}/', {
            'content': 'updated comment'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_their_own_comment(self):
        """
        Test that a user can delete their own comment.
        """
        self.client.login(username='testuser1', password='testpassword')
        response = self.client.delete(f'/comments/{self.comment1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Comment.objects.filter(id=self.comment1.id).exists())

    def test_user_cannot_delete_someone_elses_comment(self):
        """
        Test that a user cannot delete someone else's comment.
        """
        self.client.login(username='testuser2', password='testpassword')
        response = self.client.delete(f'/comments/{self.comment1.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Comment.objects.filter(id=self.comment1.id).exists())
