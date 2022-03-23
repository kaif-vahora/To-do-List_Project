from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForm
from django.contrib.auth.views import LoginView

# Create your views here.
class BaseRegisterView(SuccessMessageMixin, FormView):

    form_class = UserForm
    template_name = 'userportal/registration.html'
    success_url = "/user/userlogin/"
    # success_message = "%(name)s was created successfully"
  
    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password) 
        user.save()    
        return super().form_valid(form)

    def get_success_message(self,cleaned_data):
        username = cleaned_data["username"]
        return username + " - User created successfully..!!"

class UserLoginView(LoginView):
    template_name = 'userportal/userlogin.html'
    success_url = "userportal/home/"

def index(request):
    return render(request, 'userportal/index.html')
