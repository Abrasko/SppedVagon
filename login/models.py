from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User_based(AbstractBaseUser):
    user_name = models.CharField(max_length=80, unique=True)
    public_name = models.CharField(max_length=40)
    user_email = models.EmailField(
        verbose_name = 'email adress',
        max_length=255, 
        unique= True,
    )
    USERNAME_FIELD = 'user_name'
    EMAIL_FIELD = 'user_email'
    REQUIRED_FIELDS = ['public_name', 'user_email']

    def __str__(self):
        return self.user_name
