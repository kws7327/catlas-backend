from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='base'),
    url(r'^index', views.index, name='index'),
#   url(r'^register', views.register, name='register'),
    url(r'^login/$', views.signin, name='login'),
]