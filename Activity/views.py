from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView
from.models import Activity

# Create your views here.
class CreateActivity(CreateView):
    model = Activity
    fields = ['activity_name','activity_description']
    template_name = 'Activity/create1.html'
    success_url = '/activity/view/'

class DeleteActivity(DeleteView):
    model = Activity
    success_url = 'activity/view/'