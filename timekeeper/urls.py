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
    url(r'^$', 'chronos.views.month'),
    url(r'^/$', 'chronos.views.month'),
    url(r'^(\d{4})/(\d{1,2})/$', 'chronos.views.month'),
    # url(r'^create-assignment/$', 'chronos.views.create_assignment'),
    url(r'^delete-assignment/(\d+)/$', 'chronos.views.delete_assignment'),
    url(r'^assign-role/(\d+)/(\d+)/$', 'chronos.views.assign_role'),
    url(r'^create-user/$', 'chronos.views.create_user'),
	url(r'^admin/', include(admin.site.urls))
)

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
