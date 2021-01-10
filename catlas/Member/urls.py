from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.index, name='base'),
    url(r'^index', views.index, name='index'),
#   url(r'^register', views.register, name='register'),
    url(r'^login/$', views.signin, name='login'),
    path('members/', views.MemberList.as_view()),
    path('members/<int:pk>/', views.MemberDetail.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)