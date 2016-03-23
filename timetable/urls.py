from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'timetable.views.timetable_page', name='timetable'),
    url(r'^grouping/(?P<grouping_id>[0-9]+)', 'timetable.views.grouping_page', name='tt_grouping'),
) 
