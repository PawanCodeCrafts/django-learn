# I write this code below
from django.urls import path
from .views import home

urlpatterns = [
    path('', home),
]