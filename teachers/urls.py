from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^students/', 'teachers.views.students_page', name='students'),
    url(r'^student/(?P<student_id>[0-9]+)', 'teachers.views.student_page', name='student'),
    url(r'^teachers/', 'teachers.views.teachers_page', name='teachers'),
    url(r'^staff/', 'teachers.views.staff_page', name='staff'),
)