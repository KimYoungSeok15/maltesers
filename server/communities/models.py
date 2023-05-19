from django.db import models
from django.conf import settings
	
class Freeboard(models.Model):
    user_name = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)    
    
class Reviewboard(models.Model):
    user_name = models.CharField(max_length=100, null=True)
    Movie_title = models.CharField(max_length=100)
    genre_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)    
    