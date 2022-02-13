from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from Student_Account.models import student

# Create your views here.

def index(request):
    return HttpResponse('index page')
    #students = student.objects.all()[1:6]
    #return render(request,"index.html",{'student':students})

def student(request):
    return HttpResponse('welcome  page')
    #students = student.objects.filter(LastName__startswith='o')
    #return render(request,"index.html",{'student':students})
