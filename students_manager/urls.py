from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'students_manager.views.student_manager_page', name='student_manager'),
    url(r'^students/', 'students_manager.views.students_page', name='students'),
    url(r'^groups/(?P<group_id>[0-9]+)/edit', 'students_manager.views.groups_page', name='group_edit'),
    url(r'^groups/', 'students_manager.views.groups_page', name='groups'),
    url(r'^group/(?P<group_id>[0-9]+)', 'students_manager.views.group_page', name='group'),
    url(r'^groupings/', 'students_manager.views.groupings_page', name='groupings'),
    url(r'^grouping/(?P<grouping_id>[0-9]+)', 'students_manager.views.grouping_page', name='grouping'),
    url(r'^courses/', 'students_manager.views.courses_page', name='courses'),
    url(r'^course/(?P<course_id>[0-9]+)', 'students_manager.views.course_page', name='course'),
)