from django.db import models

from ratenyu.professors.models import Professor


class Courses(models.Model):
    courseId = models.CharField(max_length=250, primary_key=True)
    courseTitle = models.CharField(max_length=250)
    courseSubjectCode = models.CharField(max_length=20, blank = True)
    catalogNumber = models.CharField(max_length=20, blank = True)
    courseDescription = models.TextField(blank = True)

    def __str__(self):
        return self

class Class(models.Model):
    classId = models.CharField(max_length=250, primary_key=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    classType = models.CharField(max_length=250, blank = True)
    classSection = models.CharField(max_length=250, blank = True)
    term = models.CharField(max_length=250, blank = True)
    lastOffered = models.CharField(max_length=250, blank = True)
    location = models.CharField(max_length=250, blank = True)
    enrollCapacity = models.PositiveIntegerField(blank = True)

    def __str__(self):
        return self