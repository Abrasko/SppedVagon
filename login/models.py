from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)
from django.utils import timezone
# from login.registration_errors import *
# Create your models here.


class User_basedManager(BaseUserManager):
    def create_user(self, user_name, password=None):

        user = self.model(
            original_user_name=user_name,
            user_name=user_name.lower(),
            public_name=user_name,
            date_of_register=timezone.now(),
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, user_name, password):
        user = self.create_user(
            user_name,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User_based(AbstractBaseUser):
    user_name = models.CharField(max_length=80, unique=True)
    original_user_name = models.CharField(max_length=80, null=True)
    # user_image_field = models.ImageField(verbose_name='User photo')
    public_name = models.CharField(max_length=60)
    user_email = models.EmailField(
        verbose_name='email adress',
        max_length=255,
        unique=False,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = User_basedManager()

    date_of_register = models.DateField(default=timezone.now)
    user_city = models.CharField(max_length=200, default='None')

    USERNAME_FIELD = 'user_name'
    EMAIL_FIELD = 'user_email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.user_name

    def has_perm(self, perm, obj=None):

        return True

    def has_module_perms(self, app_label):

        return True

    @property
    def is_staff(self):
        return self.is_admin
