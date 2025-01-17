import datetime

from django.db import models
from django.utils import timezone

from professors.models import Professor


class Course(models.Model):
    course_id = models.CharField(max_length=250, primary_key=True)
    course_title = models.CharField(max_length=250)
    course_subject_code = models.CharField(max_length=20, blank=True)
    catalog_number = models.CharField(max_length=20, blank=True)
    course_description = models.TextField(blank=True)


class Class(models.Model):
    class_id = models.CharField(max_length=250, primary_key=True)
    professor = models.ForeignKey(to=Professor, on_delete=models.CASCADE)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    class_type = models.CharField(max_length=250, blank=True)
    class_section = models.CharField(max_length=250, blank=True)
    term = models.CharField(max_length=250, blank=True)
    last_offered = models.CharField(max_length=250, blank=True)
    location = models.CharField(max_length=250, blank=True)
    enroll_capacity = models.PositiveIntegerField(blank=True)


class Review(models.Model):
    review_text = models.TextField()
    rating = models.PositiveIntegerField(choices=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ))
    class_id = models.ForeignKey(to=Class, on_delete=models.CASCADE)
    user = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.review_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
