# STANDARD IMPORTS
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    diretoria = models.CharField(max_length=100)

    def __str__(self):
        return self.username.username
