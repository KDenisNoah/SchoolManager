from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'groups.views.main_page', name='main'),#FIXME Dirty hack to get / working
)