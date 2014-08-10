from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',

#    Account authentication
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/'}, name="logout"),
    url(r'^signup/$', views.signup, name="signup"),

#    Account management
    url(r'^edit/password/$', views.edit_password, name='edit_password'),
    url(r'^edit/$', views.edit_account, name='edit_account'),
    url(r'^view/$', views.view_account, name='view_my_account'),
    url(r'^view/(?P<username>.*)/$', views.view_account, name='view_account'),
)