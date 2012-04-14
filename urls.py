from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'timekeeper.views.home', name='home'),
    # url(r'^timekeeper/', include('timekeeper.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),,
    url(r'^$', 'timekeeper.chronos.views.index'),
    url(r'^(\d+)/(\d+)/$', 'timekeeper.chronos.views.month'),
	url(r'^admin/', include(admin.site.urls))
)