from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)

from mychar.models import ProfileParams
from django.utils import timezone

#from login.registration_errors import *
# Create your models here.
class User_basedManager(BaseUserManager):
    def create_user(self, user_name, user_email, public_name, password=None):
        
        
        # check_unique_user_name(user_name)
        # check_unique_user_email(user_email)
        # check_for_error(user_name, public_name, user_email, password)

        user = self.model(
            user_name = user_name.lower(),
            user_email = user_email.lower(),
            public_name = public_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        params = user.profileparams_set.create(holder = user)
        params.save()       
        return user

    def create_superuser(self, user_name, user_email, public_name, password):
        user = self.create_user(
            user_name,
            user_email,
            public_name,
            password=password,
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user

class User_based(AbstractBaseUser):
    user_name = models.CharField(max_length=80, unique=True)
    public_name = models.CharField(max_length=40)
    user_email = models.EmailField(
        verbose_name = 'email adress',
        max_length=255, 
        unique= True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = User_basedManager()

    USERNAME_FIELD = 'user_name'
    EMAIL_FIELD = 'user_email'
    REQUIRED_FIELDS = ['public_name', 'user_email']

    def __str__(self):
        return self.user_name
    
    def has_perm(self, perm, obj=None):
        
        return True

    def has_module_perms(self, app_label):

        return True

    @property
    def is_staff(self):
        return self.is_admin
