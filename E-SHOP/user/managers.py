
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, username, password=None, **extra_fields):
        """Creates and saves a new user"""

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        """Create and save new superuser with given details"""
        user = self.create_user(email, username, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user