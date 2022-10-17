import datetime

from django.db import models
from django.utils import timezone

from ratenyu.courses.models import Class


class Professor(models.Model):
    professor_id = models.CharField(max_length=250, primary_key=True)
    name = models.CharField(max_length=250)
    net_id = models.CharField(max_length=250)
    role = models.CharField(max_length=250)

    def __str__(self):
        return self

class Review(models.Model):
    review_text = models.TextField()
    rating = models.PositiveIntegerField(choices=[1, 2, 3, 4, 5])
    class_id = models.ForeignKey(to = Class, on_delete=models.CASCADE)
    user = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.reviewText
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)