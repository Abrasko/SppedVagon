from django.db import models
from django.conf import settings

# Create your models here.


class ProfileParams(models.Model):
    holder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    date_of_birth = models.DateField('date of birth')
    city = models.CharField(max_length=200)
    subscribe_dict = {}
    settings_dict = {}
    skills_dict = {}

    def __str__(self):
        return subscribe_list