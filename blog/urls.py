from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
