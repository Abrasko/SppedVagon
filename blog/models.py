import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=140) 
    body = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)
