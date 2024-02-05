
from collections import UserDict
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Add additional fields here
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Add any additional fields as per your requirements

    def __str__(self):
        return self.title

    @property
    def likes_count(self):
        return self.likes.count()

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Like by {self.user.username} on {self.post.title}'

