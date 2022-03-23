
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def group(request):
    return HttpResponse("group called...")

def index(request):
    context ={
        'name':'TO DO APP',            
}
    return render(request,'group/index.html',context)
    
def contactUS(request):
    context ={
        'contact_name':["arkan","prit","aman","zafar","atif"]            
}
    return render(request,'group/contactUs.html',context)    

def aboutUS(request):
    context = {
        'isActive':True,
        'age':20
    }
    return render(request,'group/aboutUs.html',context)    