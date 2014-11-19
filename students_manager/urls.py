from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'students_manager.views.student_manager_page', name='student_manager'),
    url(r'^students/', 'students_manager.views.students_page', name='students'),
    url(r'^groups/', 'students_manager.views.groups_page', name='groups'),
)