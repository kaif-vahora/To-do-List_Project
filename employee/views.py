from django.http import HttpResponse
from django.shortcuts import render

from .models import Employee

# Create your views here.
def addEmployee(request):
    emp = Employee(ename='john', eage=25,eemail='John@gmail.com',econtact=1234567890)
    emp.save()
    return HttpResponse("Employee added...")

def viewEmployee(request):
    employees = Employee.objects.all().values_list()
    print(employees)
    return render(request,'employee/view.html',{'employees':employees})   

def deleteEmployee(request):
    emp = Employee.objects.get(id =1)
    emp.delete()
    return HttpResponse("Employee Deleted....")  

def updateEmployee(request):
    emp = Employee.objects.get(id =2)
    emp.eage = 35
    emp.save()
    return HttpResponse("Employee updated....")  





