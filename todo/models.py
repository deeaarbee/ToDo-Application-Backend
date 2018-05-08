from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class TodoBoard(models.Model):

    todoid = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    description = models.TextField()
    status = models.TextField(max_length=128)
    date_created = models.DateField()

class User(AbstractUser):
    rollnumber = models.IntegerField(default=None, null=True)
