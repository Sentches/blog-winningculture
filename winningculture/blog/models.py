from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('blog:detail', kwargs={"slug":self.slug})

    class Meta:
        ordering = ("-created",)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
       ordering = ('created',)

    def __str__(self):
        return f'Comment By {self.name}'