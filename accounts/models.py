from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    choices=[['Editor','editor'],['viewer','Viewer']]
    role=models.CharField(max_length=20,choices=choices,default='viewer')
    def __str__(self):
        return self.username