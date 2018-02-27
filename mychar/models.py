from django.db import models
from django.conf import settings
from django.utils import timezone

# from login.models import User_based as User
# Create your models here.


class ProfileParams(models.Model):
    holder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    date_of_register = models.DateField(default=timezone.now())
    city = models.CharField(max_length=200, default='None')
    subscribe_dict = {}
    settings_dict = {}
    skills_dict = {}

    def __str__(self):
        return str(self.subscribe_dict)

class SkillsList(models.Model):
    skill_name = models.CharField(max_length=100, unique=True)
    skill_popularity = models.IntegerField()
    skill_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.skill_id
    
    def create_skill(self, skill_name, skill_popularity=1, skill_id=None):

        skill = self.model(
            skill_name = skill_name,
            skill_popularity = skill_popularity,
            skill_id = skill_name.lower().replace(' ', '_'),
        )

        skill.save(using=self._db)
        