from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.home', name='home'),
    url(r'^b2b$', 'b2b.views.home', name='b2b'),
    url(r'^b2c$', 'b2c.views.home', name='b2c'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
