from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'school_qms.views.qms_page', name='qms'),
    url(r'^processes/', 'school_qms.views.processes_page', name='processes'),
    url(r'^procedures/', 'school_qms.views.procedures_page', name='procedures'),
)