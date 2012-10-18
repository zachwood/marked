from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'bookmarks.views.home', name='home'),
    url(r'^save/$', 'bookmarks.views.bookmarklet_save', name="save"),

    url(r'^everyone/$', 'bookmarks.views.everyone', name="everyone"),
    url(r'^recent/$', 'bookmarks.views.recent', name="recent"),

    url(r'^mark/(?P<mark_id>\d+)/view/$', 'bookmarks.views.view_mark', name="view_mark"),
    url(r'^mark/(?P<mark_id>\d+)/update/$', 'bookmarks.views.update_mark', name="update_mark"),
    url(r'^mark/(?P<mark_id>\d+)/remove/$', 'bookmarks.views.remove_mark', name="remove_mark"),
    url(r'^mark/(?P<mark_id>\d+)/favorite/$', 'bookmarks.views.favorite_mark', name="favorite_mark"),

    url(r'^mark/(?P<mark_id>\d+)/unfavorite/$', 'bookmarks.views.unfavorite_mark', name="unfavorite_mark"),

    url(r'^profile/(?P<show_user>\w+)/$', 'bookmarks.views.user_page', name="show_user"),
    url(r'^profile/(?P<show_user>\w+)/all/$', 'bookmarks.views.all_marks', name="all_marks"),

    url(r'^profile/(?P<show_user>\w+)/favorites/$', 'bookmarks.views.view_favorites', name="view_favorites"),

    #url(r'^accounts/register/$', 'accounts.views.register', name="register"),

    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'accounts/logout.html'}),
    (r'^accounts/changepassword/$', 'django.contrib.auth.views.password_change', {'template_name': 'accounts/change_password.html'}),
    (r'^accounts/changepassword/done/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'accounts/change_password_done.html'}),

    # url(r'^marked/', include('marked.foo.urls')),

    url(r'^zeus/', include('marked.zeus.urls')),

    url(r'^404/$', direct_to_template, {'template': '404.html'}),
    url(r'^500/$', direct_to_template, {'template': '500.html'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)  

urlpatterns += staticfiles_urlpatterns()
