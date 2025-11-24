from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
# mene yeh code likha hai
from django.http import HttpResponse

# import models
from .models import *
from .forms import EmployeeForm

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
    emp = Employee.objects.get(id = id)
    # emp = get_object_or_404(Employee,id=id)
    empForm = EmployeeForm(instance=emp)
    if request.method == "POST":
        empForm = EmployeeForm(request.POST, instance=emp)
        if empForm.is_valid():
            empForm.save()

    data = {'formData':empForm, "employee": emp}
    return render(request, "employee.html", data)


def createNewEmployee(request):
    empForm = EmployeeForm()
    if request.method == "POST":
        empForm = EmployeeForm(request.POST)
        if empForm.is_valid():
            empForm.save()
            return redirect("all_employees")
    data = {'formData':empForm}
    return render(request, "employee.html", data)



def DeleteEmployeeView(request, id):
    emp = Employee.objects.get(id = id)
    emp.delete()
    return redirect("all_employees")

def ActiveEmployees(request):
    emp = Employee.objects.filter(isActive = True)
    data = {'data': emp}
    return render(request, 'all_employees.html',context=data)

def filterEmployee(request, salary):
    emp = Employee.objects.filter(salary__gte = salary)
    data = {'data': emp}
    return render(request, 'all_employees.html',context=data)
    
    
    
#  authentication
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def profile(request,id =1):
    profile = request.user
    if request.user.is_authenticated:
        return redirect('home')
    user = UserProfile.objects.get(user=profile)
    data = {'data':user}
    return render(request, 'profile.html',data)
        
def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')        
        password = request.POST.get('password')    
        user = authenticate(request=request, username=username, password=password) 
        
        if not user:
            data = {"message": "Incorrect Username or Password"}
            return render(request, 'signin.html', data)
        login(request, user=user)
        return redirect("profile")
    return render(request , 'signin.html')
            
            
               
    




