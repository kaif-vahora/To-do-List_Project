from multiprocessing import context
from django.shortcuts import render
from .models import Student

# Create your views here.
def studentData(request):

    students = Student.objects.all().values() #it will return dictonary
    students = Student.objects.all().values_list() #it will return list of tuple
    students1 = Student.objects.filter(student_name__startswith = 'x').values()
    students2 = Student.objects.filter(student_name__contains = 'a').values()
    #lookup methods......
    #students3 = Student.objects.filter(role_id__gt = 1).values()
    #students4 = Student.objects.filter(role_id__lte = 1).values()
    
    print("filter",students2)
    print(students[0].get('id'))
    print(students[0])
    studentlist = []
    for i in students1[0].values():
        studentlist.append(i)
        print('student list:',studentlist)
    for i in studentlist:
        print(i,end=',')

    context = {
        'students':studentlist
    }

    return render(request,'orm/student.html',context)