from django.db import models
from django.conf import settings


class News(models.Model):

    CATEGORY_CHOICES = [
        ('sports', 'Sports'),
        ('education', 'Education'),
        ('politics', 'Politics'),
        ('technology', 'Technology'),
    ]

    STATE_CHOICES = [
        ('andhra', 'Andhra Pradesh'),
        ('tamilnadu', 'Tamil Nadu'),
        ('telangana', 'Telangana'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()

    image = models.ImageField(upload_to='news_images/', null=True, blank=True)

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    state = models.CharField(max_length=50, choices=STATE_CHOICES)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='news_posts'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title