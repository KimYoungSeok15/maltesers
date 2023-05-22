from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator
	
class Freeboard(models.Model):
    user_name = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    Movie_title = models.CharField(max_length=100)
    genre_name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0, validators=[MaxValueValidator(10)])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)    
    
# class Reviewboard(models.Model):
#     user_name = models.CharField(max_length=100, null=True)
#     Movie_title = models.CharField(max_length=100)
#     genre_name = models.CharField(max_length=100)
#     rating = models.DecimalField(max_digits=3, decimal_places=1, default=0, validators=[MaxValueValidator(10)])
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True, null=True)
#     updated_at = models.DateTimeField(auto_now=True, null=True)    
    

# 자유게시판 댓글
class Freeboard_comment(models.Model):
    freeboard_id = models.CharField(max_length=100, null=True)
    user_name = models.CharField(max_length=100, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)   
    
# # 리뷰게시판
# class Reviewboard_comment(models.Model):
#     reviewboard = models.ForeignKey(Reviewboard, on_delete=models.CASCADE)
#     user_name = models.CharField(max_length=100, null=True)
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True, null=True)
#     updated_at = models.DateTimeField(auto_now=True, null=True)   