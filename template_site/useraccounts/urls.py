from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from . import views as app_views


urlpatterns = [
    url(r'^ulogin/$', auth_views.login, {'template_name': 'userreg/login.html'}, name='login'),
	url(r'^ulogout/$', auth_views.logout, {'template_name': 'userreg/logged_out.html'},  name='logout'),

	url(r'^upass_change/$', auth_views.password_change, {'template_name': 'userreg/password_change.html' , 'post_change_redirect' : '/useraccounts/upass_change/done/' }, name='password_change'),
	url(r'^upass_change/done/$', auth_views.password_change_done, {'template_name': 'userreg/password_change_done.html'}, name='password_change_done'),

	url(r'^upass_reset/$', auth_views.password_reset, {'template_name': 'userreg/password_reset.html' , 'post_reset_redirect' : '/useraccounts/upass_reset/done/' , 'email_template_name': 'userreg/password_reset_email.html'  }, name='password_reset'),
	url(r'^upass_reset/done/$', auth_views.password_reset_done, {'template_name': 'userreg/password_reset_done.html' }, name='password_reset_done'),

	url(r'^ureset/done/$', auth_views.password_reset_complete, {'template_name': 'userreg/password_reset_complete.html' }, name='password_reset_complete'),
	url(r'^ureset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {'template_name': 'userreg/password_reset_confirm.html' , 'post_reset_redirect' : '/ureset/done/' }, name='password_reset_confirm' ),
    
    url(r'^profile/$', app_views.get_profile , name='get_profile'),
]
