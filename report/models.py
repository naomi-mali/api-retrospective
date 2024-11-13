from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    """Model for the Report form"""

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
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='report', on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='spam')
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Order the most recent report first"""
        ordering = ['-created_at']

    def __str__(self):
        return f"Report by {self.user} - {self.category}"
