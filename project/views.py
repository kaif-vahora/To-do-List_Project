from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def addproject(request):
    print("addproject called...")
    return HttpResponse("addproject called...")

#create view project function to display the project page
def viewproject(request):
    return HttpResponse("viewproject called...")

#create view project function to display the project page
def projectpage(request):
    return render(request,'project/projectpage.html')    



