# I write this code below
from django.urls import path
from myApp import views

urlpatterns = [
   path('',views.product),
   path('1/',views.product1),
     
]
