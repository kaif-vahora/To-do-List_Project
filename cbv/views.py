from django.views.generic import ListView
from django.shortcuts import render
from .models import Hr

# Create your views here.
class HrList(ListView):
    model = Hr
    hrlist = model.objects.all()
    template_name = 'cbv/hr_list.html'
    context_object_name = 'hrlist'

