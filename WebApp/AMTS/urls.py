from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^login', views.login, name='login'),
    url(r'^reports/machine_search', csrf_exempt(views.machine_search), name='machine_search'),
    url(r'reports/$', views.reports, name='reports'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^test', views.my_view)
]
