from django.db import models

from ratenyu.professors.models import Professor

# Create your models here.
class Courses(models.Model):
    courseTitle = models.CharField(max_length=250)
    courseDescription = models.TextField(blank = True)

    def __str__(self):
        return self
class Class(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    classType = models.CharField(max_length=250, blank = True)
    classNumber = models.PositiveIntegerField(blank = True)
    classSection = models.CharField(max_length=250, blank = True)
    term = models.CharField(max_length=250, blank = True)
    lastOffered = models.CharField(max_length=250, blank = True)
    location = models.CharField(max_length=250, blank = True)
    classDescription = models.TextField(blank = True)
    capacity = models.PositiveIntegerField(blank = True)
    
    def __str__(self):
        return self