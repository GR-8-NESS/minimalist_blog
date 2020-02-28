from django.db import models
from django.utils import timezone
from users.models import UserProfile

from taggit.managers import TaggableManager
# Create your models here.


class Post(models.Model):
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    title = models.CharField(blank=False, max_length=120)
    body = models.TextField()
    author = models.ForeignKey(UserProfile, on_delete= models.CASCADE) 
    date_created = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()

    def __str__(self):
        return f'{self.title}'
"""
Subject to removal still don't know why i need a draft
"""
class Draft(models.Model):
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    title = models.CharField(blank=False, max_length=120)
    body = models.TextField()
    author = models.ForeignKey(UserProfile, on_delete= models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete= models.CASCADE, null=True, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return f'{self.title}'
