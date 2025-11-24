from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# yeh mene likha hai 

class Student(models.Model):
    roll_No = models.IntegerField()
    name = models.CharField(max_length=50)
    desc = models.TextField()
    isActive = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.roll_No} --> {self.name}'
    
    
    # unique --> data unique ho
    # default --->data default lene ke liye
    # blank=True ---> khali field rakhni ki nhi 
    
class Customer(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.name} {self.city}'
    
class Employee(models.Model):
    name = models.CharField(max_length = 20)
    salary = models.IntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits = 5,decimal_places=2, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    isActive = models.BooleanField(default = True)
    
    def __str__(self):
        return self.name
    

# user profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    # profileImage = models.ImageField(null=True, blank=True, upload_to="user/", height_field=None, width_field=None, max_length=None)

    