from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'bookmarks.views.home', name='home'),
    url(r'^save/$', 'bookmarks.views.bookmarklet_save', name="save"),

    #url(r'^accounts/register/$', 'accounts.views.register', name="register"),

    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'accounts/logout.html'}),
    (r'^accounts/changepassword/$', 'django.contrib.auth.views.password_change', {'template_name': 'accounts/change_password.html'}),
    (r'^accounts/changepassword/done/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'accounts/change_password_done.html'}),

    # url(r'^marked/', include('marked.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)  

urlpatterns += staticfiles_urlpatterns()
