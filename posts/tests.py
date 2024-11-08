from django.contrib.auth.models import User
from .models import Post, Report
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')
        User.objects.create_user(username='brian', password='pass')

    def test_can_list_posts(self):
        adam = User.objects.get(username='adam')
        Post.objects.create(owner=adam, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post('/posts/', {'title': 'a title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post('/posts/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_search_posts_by_title(self):
        adam = User.objects.get(username='adam')
        Post.objects.create(owner=adam, title='a searchable title')
        response = self.client.get('/posts/', {'search': 'searchable'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

def test_can_filter_posts_by_owner(self):
    """Test filtering posts by owner (username)"""
    adam = User.objects.get(username='adam')
    Post.objects.create(owner=adam, title='adam post')
    brian = User.objects.get(username='brian')
    Post.objects.create(owner=brian, title='brian post')
    response = self.client.get('/posts/', {'owner_username': 'adam'})
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)


class PostDetailViewTests(APITestCase):
    """Post detail view tests"""

    def setUp(self):
        self.adam = User.objects.create_user(username='adam', password='pass')
        self.brian = User.objects.create_user(username='brian', password='pass')
        self.post1 = Post.objects.create(owner=self.adam, title='a title')
        self.post2 = Post.objects.create(owner=self.brian, title='another title')

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get(f'/posts/{self.post1.id}/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put(f'/posts/{self.post1.id}/', {'title': 'a new title'})
        self.post1.refresh_from_db()
        self.assertEqual(self.post1.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put(f'/posts/{self.post2.id}/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.delete(f'/posts/{self.post1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Post.objects.filter(id=self.post1.id).exists())

    def test_user_cant_delete_another_users_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.delete(f'/posts/{self.post2.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ReportPostViewTests(APITestCase):
    """Test reporting posts"""

    def setUp(self):
        self.adam = User.objects.create_user(username='adam', password='pass')
        self.brian = User.objects.create_user(username='brian', password='pass')
        self.post = Post.objects.create(owner=self.adam, title='Post to Report')

    def test_user_can_report_post(self):
        self.client.login(username='adam', password='pass')
        data = {'post': self.post.id, 'reason': 'spam', 'category': 'harassment'}
        response = self.client.post('/reports/', data)
        print(response.data)  # To debug response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_cant_report_same_post_twice(self):
        self.client.login(username='adam', password='pass')
        data = {'post': self.post.id, 'reason': 'spam', 'category': 'harassment'}
        self.client.post('/reports/', data)
        response = self.client.post('/reports/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_not_logged_in_cant_report_post(self):
        data = {'post': self.post.id, 'reason': 'spam', 'category': 'harassment'}
        response = self.client.post('/reports/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class MentionsListViewTests(APITestCase):
    """Test mentions list"""

    def setUp(self):
        self.adam = User.objects.create_user(username='adam', password='pass')
        self.brian = User.objects.create_user(username='brian', password='pass')

    def test_can_get_mentions_for_existing_user(self):
        response = self.client.get('/mentions/', {'search': 'adam'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_can_get_empty_mentions_for_non_existing_user(self):
        response = self.client.get('/mentions/', {'search': 'nonexistentuser'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
