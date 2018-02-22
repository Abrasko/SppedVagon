from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_default(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_nick = models.CharField(max_length=100)

    def __str__(self):
        return self.user_nick
