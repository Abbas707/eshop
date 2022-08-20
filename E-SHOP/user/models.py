from django.db import models
from django.contrib.auth.models import AbstractUser
from user.managers import UserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=11, blank=True, null=True)

    objects = UserManager()

    # sign up user using email and name
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
      return str(self.username)
