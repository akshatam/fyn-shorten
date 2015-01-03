from django.conf.urls import patterns, include, url
from django.contrib import admin
from shorten import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tinyurl.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'shorten.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^submit/$', 'shorten.views.submit'),
)
