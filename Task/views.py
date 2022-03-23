from urllib import request
from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from.models import Task
from django.views.generic import DetailView
# Create your views here.
class CreateTask(CreateView):
    model = Task
    fields = ['task_name','task_description']
    template_name = 'Task/create.html'
    success_url = '/task/view/'

class DeleteTask(DeleteView):
    model = Task
    success_url = 'task/view/'

def index(request):
    return render(request,'Task/index.html')

class UpdateTask(UpdateView):
    model = Task
    fields = ['task_name','task_description']
    template_name = 'Task/update.html'
    success_url = '/task/view/'

class TaskDetail(DetailView):
    model = Task
    template_name = 'Task/task_detail.html'

    



    
   

