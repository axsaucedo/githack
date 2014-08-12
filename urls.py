from django.conf.urls import patterns, url, include
from settings import STATIC_ROOT, MEDIA_ROOT

from django.contrib import admin
admin.autodiscover()

handler404 = 'githack.views.error404'
handler500 = 'githack.views.error500'

urlpatterns = patterns('',

    #My Apps
    url(r'accounts/', include('accounts.urls')),
    url(r'', include('githack.urls')),

    #External Apps
    url(r'', include('social_auth.urls')),

    #Admin
    ('^admin/', include(admin.site.urls)),

    #Static files
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)
