from django.db import models
from django.conf import settings
from django.utils import timezone

from login.models import User_based as User

from mychar.backend import path_and_rename

# from login.models import User_based as User
# Create your models here.


class CharPost(models.Model):
    post_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    post_text = models.TextField(max_length=2000)
    post_date = models.DateTimeField('Post publication date')

    def __str__(self):
        answer = ('(By ' + self.post_author.user_name + ', post_id=' +
                  str(self.id) + ')\n' + self.post_text)
        return answer


class CharPostComment(models.Model):
    post = models.ForeignKey(
        CharPost,
        on_delete=models.CASCADE,
    )
    comment_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    comment_text = models.TextField(max_length=1000)
    comment_date = models.DateTimeField('Comment publication date')

    def __str__(self):
        return self.comment_text

        return str(self.subscribe_dict)


class CharPhoto(models.Model):
    photo_author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        upload_to=path_and_rename,
        height_field="image_height",
        width_field="image_width",
        null=True,
        blank=True,
        editable=True,
        help_text="Profile Picture",
        verbose_name="Profile Picture"
    )
    photo_date = models.DateTimeField(default=timezone.now)
    is_char_photo = models.BooleanField(default=False)
    image_height = models.PositiveIntegerField(
        null=True, blank=True, editable=False, default="300")
    image_width = models.PositiveIntegerField(
        null=True, blank=True, editable=False, default="200")


class AllSkillsList(models.Model):
    skill_name = models.CharField(max_length=100, unique=True)
    skill_popularity = models.IntegerField()
    skill_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.skill_id

    def create_skill(self, skill_name, skill_popularity=1, skill_id=None):

        skill = self.model(
            skill_name=skill_name,
            skill_popularity=skill_popularity,
            skill_id=skill_name.lower().replace(' ', '_'),
        )

        skill.save(using=self._db)


class UserSkillsList(models.Model):
    holder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    skill_id = models.CharField(max_length=100, unique=False)
    skill_points = models.IntegerField()


class UserSettingsList(models.Model):
    holder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    setting_id = models.CharField(max_length=200, unique=False)
    setting_value = models.FloatField()


class UserSubscribesList(models.Model):
    holder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    subscribe_id = models.CharField(max_length=100)
    subscribe_date = models.DateTimeField('date since subscribed')
