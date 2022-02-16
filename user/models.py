from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class Initials(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)


class User(AbstractBaseUser):
    email = models.EmailField(max_length=64)
    password = models.CharField(max_length=32)
    username = models.CharField(max_length=32, unique=True)

    initials = models.ForeignKey(Initials, on_delete=models.CASCADE)
    birth = models.DateField()

    created = models.DateTimeField(auto_now_add=True)
    visited = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "username"
