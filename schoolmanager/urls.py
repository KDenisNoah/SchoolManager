from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'schoolmanager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'students_manager.views.home_page', name='home'),
    #url(r'^admin/', include(admin.site.urls)),
)
