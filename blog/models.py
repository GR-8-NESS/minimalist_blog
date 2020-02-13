from django.db import models
from django.utils import timezone
from users.models import UserProfile
# Create your models here.


class Posts(models.Model):
    slug = models.SlugField()
    title = models.CharField(blank=False, max_length=120)
    body = models.TextField()
    author = models.ForeignKey(UserProfile, on_delete= models.CASCADE) 
    date_created = models.DateTimeField(default=timezone.now)
    #tags =
"""
Subject to removal still don't know why i need a draft
"""
class Draft(models.Model):
    slug = models.SlugField()
    title = models.CharField(blank=False, max_length=120)
    body = models.TextField()
    author = models.ForeignKey(UserProfile, on_delete= models.CASCADE)
    post_id = models.ForeignKey(Posts, on_delete= models.CASCADE)
    #tags = 
