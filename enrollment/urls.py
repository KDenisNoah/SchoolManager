from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'groups.views.main_page', name='main'),#FIXME Dirty hack to get / working
    url(r'^subjects/', 'enrollment.views.subjects_page', name='subjects'),
    url(r'^enrollments/', 'enrollment.views.enrollments_page', name='enrollments'),
)