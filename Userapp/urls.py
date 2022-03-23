from django.contrib import admin
from django.urls import include, path
from .views import * 
from . import views
# app_name = 'project_urls'


urlpatterns = [
    path('userregistration/',BaseRegisterView.as_view(),name='userregistration'),
    path('userlogin/',UserLoginView.as_view(),name='userlogin'),
    path("index/",views.index)
]