from django.db import models
import datetime
from django.utils import timezone

from ratenyu.courses.models import Class

# Create your models here.
class Professor(models.Model):
    name = models.CharField(max_length=250)
    netId = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    
    def __str__(self):
        return self
class Review(models.Model):
    reviewText = models.TextField()
    rating = models.PositiveIntegerField(choices=[1, 2, 3, 4, 5])
    classKey = models.ForeignKey(Class, on_delete=models.CASCADE)
    user = models.CharField(max_length=250)
    pubDate = models.DateTimeField('date published')
    
    def __str__(self):
        return self.reviewText
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)