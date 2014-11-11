from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'schoolmanager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'students_manager.views.home_page', name='home'),
    url(r'^students/', 'students_manager.views.students_page', name='students'),
    url(r'^groups/', 'students_manager.views.groups_page', name='groups'),
    #url(r'^admin/', include(admin.site.urls)),
)
