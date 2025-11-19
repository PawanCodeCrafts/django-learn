from django.shortcuts import render, get_object_or_404

# Create your views here.
# mene yeh code likha hai
from django.http import HttpResponse

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

def employee_detail_view(request,id):
    # return HttpResponse(f'<h1>{id}</h1>')
    emp = Employee.objects.get(id = id)
    # emp = get_object_or_404(Employee,id=id)
    if request.method == "POST":
        salary = request.POST.get('salary')
        emp.salary = salary
    data = {'employee' : emp}
    return render(request, 'employee.html',data)

def ActiveEmployees(request):
    emp = Employee.objects.filter(isActive = True)
    data = {'data': emp}
    return render(request, 'all_employee.html',context=data)

def filterEmployee(request, salary):
    emp = Employee.objects.filter(salary__gte = salary)
    data = {'data': emp}
    return render(request, 'all_employee.html',context=data)
    
    




