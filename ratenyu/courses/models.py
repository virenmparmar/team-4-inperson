from django.db import models

from ratenyu.professors.models import Professor


class Courses(models.Model):
    course_id = models.CharField(max_length=250, primary_key=True)
    course_title = models.CharField(max_length=250)
    course_subject_code = models.CharField(max_length=20, blank=True)
    catalog_number = models.CharField(max_length=20, blank=True)
    course_description = models.TextField(blank=True)

    def __str__(self):
        return self

class Class(models.Model):
    class_id = models.CharField(max_length=250, primary_key=True)
    professor = models.ForeignKey(to = Professor, on_delete=models.CASCADE)
    course = models.ForeignKey(to = Courses, on_delete=models.CASCADE)
    class_type = models.CharField(max_length=250, blank=True)
    class_section = models.CharField(max_length=250, blank=True)
    term = models.CharField(max_length=250, blank=True)
    last_offered = models.CharField(max_length=250, blank=True)
    location = models.CharField(max_length=250, blank=True)
    enroll_capacity = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self