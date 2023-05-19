
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass


class Profile(models.Model):
    user_name = models.CharField(max_length=100, null=True)
    last_login = models.DateField()
    date_joined = models.DateField()
    
    
class Following(models.Model):
    user_name = models.CharField(max_length=100, null=True)
    following = models.CharField(max_length=100, null=True)