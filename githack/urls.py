from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

<<<<<<< HEAD
    # Home
#    url(r'^$', 'githack.views.home', name='home'),

    # API
=======
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
>>>>>>> 7801a4311ba9a6b360342ec24dfa6789df94acec

    url(r'^admin/', include(admin.site.urls)),
)
