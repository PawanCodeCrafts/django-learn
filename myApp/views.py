from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# I write this code below

def product(request):
    return HttpResponse('this is product page')
def product1(request):
    return HttpResponse('this is product 1 page')