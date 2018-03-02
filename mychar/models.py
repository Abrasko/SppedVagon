from django.db import models
from django.conf import settings
from django.utils import timezone

# from login.models import User_based as User
# Create your models here.


class BasePost(models.Model):
    post_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    post_text = models.TextField(max_length=2000)
    post_date = models.DateTimeField('Post publication date')

    def __str__(self):
        return self.post_text


class BaseComment(models.Model):
    post = models.ForeignKey(
        BasePost,
        on_delete = models.CASCADE,
    )
    comment_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    comment_text = models.TextField(max_length=1000)
    comment_date = models.DateTimeField('Comment publication date')

    def __str__(self):
        return self.comment_text

        return str(self.subscribe_dict)

class AllSkillsList(models.Model):
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
        
class UserSkillsList(models.Model):
    holder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )

    skill_id = models.CharField(max_length=100, unique=True)
    skill_points = models.IntegerField()


class UserSettingsList(models.Model):
    holder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    
    setting_id = models.CharField(max_length=200, unique=True)
    setting_value = models.FloatField()

class UserSubscribesList(models.Model):
    holder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )

    subscribe_id = models.CharField(max_length=100)
    subscribe_date = models.DateTimeField('date since subscribed')