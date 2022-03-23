from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView

# Create your views here.
class UserLogin(LoginView):
    template_name = 'core/login.html'

class UserLogout(LogoutView):
    pass

class Register(CreateView):
    template_name = 'core/signup.html'
    success_url = '/admin'

    
    