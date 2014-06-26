from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'books.views.display_request_info', name='home'),
    url(r'^display_meta/$', 'books.views.display_meta', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$', 'books.views.search', name='search'),
)
