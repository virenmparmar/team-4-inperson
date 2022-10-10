from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:course_id>/course_result_by_id', views.course_result_by_id, name='course_result_by_id'),
    path('<str:professors_name>/professors_result', views.professors_result, name='professors_result'),
    path('<str:course_name>/course_result_by_name', views.course_result_by_name, name='course_result_by_name'),
]
