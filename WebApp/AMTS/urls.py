from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^login', views.login, name='login'),
    url(r'reports', views.reports, name='reports'),
]
