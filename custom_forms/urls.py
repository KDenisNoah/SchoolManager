from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'students_manager.views.student_manager_page', name='student_manager'),
    url(r'^forms/', 'custom_forms.views.forms_page', name='forms'),
    url(r'^form/(?P<form_id>[0-9]+)', 'custom_forms.views.form_page', name='form'),
    url(r'^questions/', 'custom_forms.views.questions_page', name='questions'),
)