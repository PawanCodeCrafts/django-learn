from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        # fields = ['name', 'weight','email']
        fields = '__all__'