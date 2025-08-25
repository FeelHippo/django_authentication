from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_anonymous = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=False)