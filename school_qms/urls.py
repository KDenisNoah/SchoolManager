from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'school_qms.views.qms_page', name='qms'),
    url(r'^processes/', 'school_qms.views.processes_page', name='processes'),
    url(r'^procedures/', 'school_qms.views.procedures_page', name='procedures'),
    url(r'^documents/', 'school_qms.views.documents_page', name='documents'),
    url(r'^document/(?P<doc_id>[0-9]+)/edit$',
    'school_qms.views.documents_page', name='document'),
    url(r'^document/(?P<doc_id>[0-9]+)/$', 'school_qms.views.document_page',
         name='document'),
    url(r'^agents/', 'school_qms.views.add_agent', name='agents'),
    url(r'^recipients/', 'school_qms.views.add_recipient', name='recipients'),
    url(r'^revisions/(?P<doc_id>[0-9]+)/$', 'school_qms.views.add_revision',
         name='revision'),
    url(r'^revisions/', 'school_qms.views.add_revision', name='revisions'),
)