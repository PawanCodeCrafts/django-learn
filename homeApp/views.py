from django.shortcuts import render

# Create your views here.
# mene yeh code likha hai
# from django.http import HttpResponse

from .models import *
# import models

def home(request):
    username = "Pawan"
    context = {'username': username} 
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def all_employee(request):
    # emp = models.Employee.objects.all()
    emp = Employee.objects.all()
    data = {'data': emp}
    return render(request, 'all_employee.html',context = data)




