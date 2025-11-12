from django.shortcuts import render

# Create your views here.
# mene yeh code likha hai
from django.http import HttpResponse

def home(request):
    name = "pawan"
    age = 21
    dogs = ['dog1', 'dog2']
    info = {"degree": "B.Tech", "college": "RJIT", "job": "Netmax"}
    isActive = False 

    di = {
        'name': name,
        'age': age,
        'dogs': dogs,
        'info': info,
        'active': isActive
    }

    return render(request, "base.html", context=di)

def about(request):
    return render(request, 'about.html')

