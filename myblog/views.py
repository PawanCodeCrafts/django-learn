from django.shortcuts import render

# Create your views here.

# I write this code below

from django.http import HttpResponse

def home(request):
    return HttpResponse('hello')
    
def about(request):
    return HttpResponse('about')
    