from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('employees/<int:id>', views.employee_detail_view, name ='employee'),
    path('employees/salary/<int:salary>',views.filterEmployee),
    path('employees/',views.all_employee, name='employees'),
    path('activeEmp/',views.ActiveEmployees),
    
]
