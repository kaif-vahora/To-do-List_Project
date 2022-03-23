from pyexpat import model
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Address
from .forms import AddressForm

# Create your views here.
class CreateAddress(CreateView):
    form_class = AddressForm
    model = Address
    template_name = 'address/address_form.html'
    success_url = '/'
