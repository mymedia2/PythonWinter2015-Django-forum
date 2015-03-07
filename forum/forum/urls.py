from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Example:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'forum.views.home'),

    url(r'^register/', 'forum.views.register'),
    url(r'^login/', 'forum.views.login'),
    url(r'^logout/', 'forum.views.logout'),

    url(r'^forum/', 'main.views.forum'),

    url(r'^admin/', include(admin.site.urls)),
)
