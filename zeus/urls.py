from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'zeus.views.home', name='zeus_home'),
    url(r'^users/$', 'zeus.views.list_users', name='zeus_list_users'),
)
