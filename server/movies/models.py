from django.db import models
from django.conf import settings
	
class Genre(models.Model):
    name = models.CharField(max_length=50)
    
class Movie(models.Model):
    adult = models.BooleanField()
    backdrop_path = models.CharField(max_length=200, null=True)
    genre_ids = models.ManyToManyField(Genre)
    movie_id = models.IntegerField()
    original_language = models.CharField(max_length=30)
    original_title = models.CharField(max_length=200)
    overview = models.TextField()
    popularity = models.DecimalField(max_digits=10, decimal_places=3)
    poster_path = models.URLField(max_length=200)
    release_date = models.DateField()
    title = models.CharField(max_length=100)
    video = models.CharField(max_length=100, null=True)
    vote_average = models.DecimalField(max_digits=10, decimal_places=1)
    vote_count = models.IntegerField(default=0)

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    
