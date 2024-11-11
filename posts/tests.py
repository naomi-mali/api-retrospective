from django.contrib.auth.models import User
from posts.models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        # Create a user for testing
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_posts(self):
        # Ensure that posts can be listed
        adam = User.objects.get(username='adam')
        post = Post.objects.create(owner=adam, title='a title', description='some description')

        # Fetch the list of posts
        response = self.client.get('/posts/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Handle possible pagination by checking for 'results' key
        posts_data = response.data.get('results', response.data)  # Use 'results' for paginated response
        
        self.assertGreater(len(posts_data), 0)  # Ensure posts are returned
        self.assertEqual(posts_data[0]['title'], 'a title')  # Validate post content

    def test_logged_in_user_can_create_post(self):
        # Ensure that a logged-in user can create a post
        self.client.login(username='adam', password='pass')
        response = self.client.post('/posts/', {'title': 'a title', 'description': 'some description'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        post = Post.objects.first()
        self.assertEqual(post.title, 'a title')
        self.assertEqual(post.description, 'some description')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        # Ensure that a non-logged-in user cannot create a post
        response = self.client.post('/posts/', {'title': 'a title', 'description': 'some description'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        # Create users and posts for testing
        adam = User.objects.create_user(username='adam', password='pass')
        brian = User.objects.create_user(username='brian', password='pass')
        Post.objects.create(
            owner=adam, title='a title', description='adams description'
        )
        Post.objects.create(
            owner=brian, title='another title', description='brians description'
        )

    def test_can_retrieve_post_using_valid_id(self):
        # Ensure that a post can be retrieved using a valid ID
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.data['description'], 'adams description')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        # Ensure that an invalid post ID returns a 404 error
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        # Ensure that a user can update their own post
        self.client.login(username='adam', password='pass')
        response = self.client.put('/posts/1/', {'title': 'a new title', 'description': 'updated description'})
        post = Post.objects.get(pk=1)
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(post.description, 'updated description')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        # Ensure that a user cannot update another user's post
        self.client.login(username='adam', password='pass')
        response = self.client.put('/posts/2/', {'title': 'a new title', 'description': 'updated description'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
