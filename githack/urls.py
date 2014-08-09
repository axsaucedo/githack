from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Home
#    url(r'^$', 'githack.views.home', name='home'),
    (r'^$', TemplateView.as_view(template_name='home/index.html')),

    url(r'^admin/', include(admin.site.urls)),
)
