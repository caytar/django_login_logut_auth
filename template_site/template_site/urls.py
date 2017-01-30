from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^useraccounts/', include('useraccounts.urls',namespace='useraccounts',app_name='useraccounts')),
    url(r'^$', RedirectView.as_view(permanent=False, url='/useraccounts/ulogin/')),
]
