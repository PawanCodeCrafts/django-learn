from django.contrib import admin

# Register your models here.

# yeh mene likha hai 
# from .models import modelkanaam
# admin.site.register(modelkanaam)

from .models import Student, Customer, Employee, UserProfile


admin.site.register(Student)
admin.site.register(Customer)
admin.site.register(Employee) 
admin.site.register(UserProfile) 

