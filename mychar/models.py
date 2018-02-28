from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


class ProfileParams(models.Model):
    holder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    date_of_birth = models.DateField('date of birth')
    city = models.CharField(max_length=200)
    subscribe_list = {}
    settings_list = {}

    def __str__(self):
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

