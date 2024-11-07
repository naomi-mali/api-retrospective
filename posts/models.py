from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    A model representing posts on the Retrospective platform.
    """
    categories = [
        ('family-and-friends', 'Family and Friends'),
        ('everyday-life-&-candid-moments', 'Everyday Life & Candid Moments'),
        ('nature-and-landscapes', 'Nature and Landscapes'),
        ('cityscapes-and-architecture', 'Cityscapes and Architecture'),
        ('food-and-drinks', 'Food and Drinks'),
        ('people-and-portraits', 'People and Portraits'),
        ('fashion-and-style', 'Fashion and Style'),
        ('travel-and-adventure', 'Travel and Adventure'),
        ('art-and-creativity', 'Art and Creativity'),
        ('fitness-and-health', 'Fitness and Health'),
        ('technology-and-gadgets', 'Technology and Gadgets'),
        ('pets-and-animals', 'Pets and Animals'),
        ('events-and-celebrations', 'Events and Celebrations'),
        ('abstract-and-conceptual', 'Abstract and Conceptual'),
        ('seasonal-and-holiday', 'Seasonal and Holiday'),
        ('vintage-and-retro', 'Vintage and Retro'),
        ('self-portraits', 'Self-Portraits'),
        ('street-photography', 'Street Photography'),
        ('relationships', 'Relationships'),
        ('other', 'Other'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=512, null=True, blank=True)
    mentioned_users = models.ManyToManyField(User, related_name='mentioned_in', blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_post_x1mf4x',
        blank=True
    )
    tagged_users = models.ManyToManyField(
        User, related_name='tagged_posts',
        blank=True
    )
    category = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        default=None,
        choices=categories
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'


class Report(models.Model):
    """
    A model for reporting inappropriate or objectionable posts.
    """
    CATEGORY_CHOICES = [
        ('spam', 'Spam'),
        ('inappropriate_content', 'Inappropriate Content'),
        ('harassment', 'Harassment or Bullying'),
        ('hate_speech', 'Hate Speech'),
        ('misinformation', 'Misinformation'),
        ('copyright_violation', 'Copyright Violation'),
        ('impersonation', 'Impersonation'),
        ('self_harm', 'Self-harm or Suicide'),
        ('other', 'Other'),
    ]

    post = models.ForeignKey(
        Post,
        related_name='reports',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    user = models.ForeignKey(User, related_name='reports', on_delete=models.CASCADE)
    reason = models.TextField()
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        blank=True,
        null=True,
        default=None,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['post', 'user'], name='unique_report_per_user_post')
        ]

    def __str__(self):
        return f'Report by {self.user} on {self.post}'
