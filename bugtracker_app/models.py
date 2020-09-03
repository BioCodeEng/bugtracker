from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    displayname = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    url = models.URLField(null=True)

    def __str__(self):
        return self.username
