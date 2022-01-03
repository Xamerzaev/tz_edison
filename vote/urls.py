from django.urls import include, re_path

from . import views

urlpatterns = [
    re_path('', views.LoginView.as_view(), name='login'),
    re_path(r'^register/$', views.RegisterView.as_view(), name='register'),
    re_path(r'^$', views.MainView.as_view(), name='main'),
    re_path(r'^first/$', views.FirstView.as_view(), name='first'),
    re_path(r'^second/(?P<pk>[0-9]+)/$', views.SecondPhaseView.as_view(), name='second'),
    re_path(r'^reset/(?P<pk>[0-9]+)/$', views.ResetView.as_view(), name='reset'),
    re_path(r'^dashboard/$', views.get_data_dashboard, name='dashboard'),
]