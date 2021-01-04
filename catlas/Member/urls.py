from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='base'),
    url(r'^index', views.index, name='index'),
#   url(r'^register', views.register, name='register'),
    url(r'^login/$', views.signin, name='login'),
    path('members/', views.Member_list),
    path('members/<int:pk>/', views.Member_detail),

]