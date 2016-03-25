from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'groups.views.main_page', name='main'),#FIXME Dirty hack to get / working
    url(r'^groups/(?P<group_id>[0-9]+)/edit', 'groups.views.groups_page', name='group_edit'),
    url(r'^groups/', 'groups.views.groups_page', name='groups'),
    url(r'^group/(?P<group_id>[0-9]+)', 'groups.views.group_page', name='group'),
    url(r'^groupings/', 'groups.views.groupings_page', name='groupings'),
    url(r'^grouping/(?P<grouping_id>[0-9]+)', 'groups.views.grouping_page', name='grouping'),
    url(r'^courses/', 'groups.views.courses_page', name='courses'),
    url(r'^course/(?P<course_id>[0-9]+)', 'groups.views.course_page', name='course'),
)