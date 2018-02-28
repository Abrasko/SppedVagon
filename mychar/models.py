from django.db import models
from django.conf import settings
from django.utils import timezone
<<<<<<< HEAD
=======

# from login.models import User_based as User
>>>>>>> 2a3752844ce80360a4460ba257354c495cdc7e2f
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
<<<<<<< HEAD
        return self.subscribe_list


class PostBased(models.Model):
    post_author = models.CharField(max_length=100)
    post_text = models.CharField(max_length=1500)
    post_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.post_text


class CommentsBased(models.Model):
    post = models.ForeignKey(
        PostBased,
        on_delete = models.CASCADE,
    )
    comment_author = models.CharField(max_length=100)
    comment_text = models.CharField(max_length=1000)
    comment_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.comment_text

=======
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
        
>>>>>>> 2a3752844ce80360a4460ba257354c495cdc7e2f
