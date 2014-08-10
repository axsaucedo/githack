from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Home
#    url(r'^$', 'githack.views.home', name='home'),
    (r'^$', TemplateView.as_view(template_name='home/index.html')),
    (r'^download/$', TemplateView.as_view(template_name='home/download.html')),

    # API
    url(r'^usercommit/$', 'githack.views.usercommit', name='user_commit'),

    url(r'^admin/', include(admin.site.urls)),
)
