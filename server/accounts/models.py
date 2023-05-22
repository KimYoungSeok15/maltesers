
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class User(AbstractUser):
    pass


class Profile(models.Model):
    user_name = models.CharField(max_length=100, null=True)
    date_joined = models.DateTimeField()
    point = models.IntegerField()
    profile_pic = models.ImageField(blank=True, null=True, upload_to='images/')
    
# 유저가 좋아하는 장르
class UserLikeGenre(models.Model):
    user_name = models.CharField(max_length=100, null=True)
    genre_name = models.CharField(max_length=30, null=True)

# 유저가 좋아요 누른 영화
class UserLikeMovie(models.Model):
    user_name = models.CharField(max_length=100, null=True)
    movie_name = models.CharField(max_length=30, null=True)
    movie_id = models.CharField(max_length=30, null=True)
    
# 전체 팔로우 목록
class Following(models.Model):
    user_name = models.CharField(max_length=100, null=True)
    following = models.CharField(max_length=100, null=True)

# 전체 좋아요 목록
class Likes(models.Model):
    user_name = models.CharField(max_length=100, null=True)
    movie_id = models.CharField(max_length=100, null=True)
    movie_name = models.CharField(max_length=100, null=True)

# 전체 픽한 영화 목록
class Pick_movies(models.Model):
    user_name = models.CharField(max_length=100, null=True)
    movie_id = models.CharField(max_length=100, null=True)
    movie_name = models.CharField(max_length=100, null=True)