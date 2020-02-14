from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Draft, Post
# Register your models here.

@admin.register(Draft)
class DraftAdmin(ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

@admin.register(Post)
class PostAdmin(ModelAdmin):
    prepopulated_fields = {'slug':('title',)}