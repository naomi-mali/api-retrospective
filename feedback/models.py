from django.db import models


class Feedback(models.Model):
    """Model for the feedback form."""
    
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=25, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Order the most recent feedback first."""
        ordering = ['-created_at']

    def __str__(self):
        return self.content
