import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=1000) 
    body = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)


class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    date = models.DateTimeField()
    body = models.TextField(max_length=250)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.body
    
    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)