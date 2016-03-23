from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^students/', 'orgperson.views.students_page', name='students'),
    url(r'^student/(?P<student_id>[0-9]+)', 'orgperson.views.student_page', name='student'),
    url(r'^teachers/', 'orgperson.views.teachers_page', name='teachers'),
    url(r'^staff/', 'orgperson.views.staff_page', name='staff'),
)