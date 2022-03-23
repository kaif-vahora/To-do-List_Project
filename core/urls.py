from atexit import register
from django.contrib import admin
from django.urls import include, path
from .views import UserLogin, UserLogout,Register

urlpatterns = [
    path("login/",UserLogin.as_view(),name="login"),
    path("logout/",UserLogout.as_view(),name="logout"),
    path('register',Register.as_view(),name="register"),
  

]