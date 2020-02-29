from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User

from users.models import UserProfile

from taggit.managers import TaggableManager
# Create your models here.


class Post(models.Model):
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    title = models.CharField(blank=False, max_length=120)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE) 
    date_created = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()

    def __str__(self):
        return f'{self.title}'
"""
Subject to removal still don't know why i need a draft
"""
class Draft(models.Model):
    slug = models.SlugField( max_length=100, unique=True, blank=True, null=True)
    title = models.CharField(blank=False, max_length=120)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete= models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('user_drafts', kwargs={'username': self.author.username})