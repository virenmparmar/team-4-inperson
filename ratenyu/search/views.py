from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("this is home/search page")


def course_result_by_id(request, course_id):
    return HttpResponse("You're looking at course %s." % course_id)


def course_result_by_name(request, course_name):
    return HttpResponse("You're looking at course %s." % course_name)


def professors_result(request, professors_name):
    return HttpResponse("You're looking at professor %s." % professors_name)
