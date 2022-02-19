from django.db import models 
from django.contrib.auth.models import AbstractUser   

class Student(models.Model):    
  name = models.CharField(max_length=225)     
  email = models.CharField(max_length=225, unique=True)   
  password = models.CharField(max_length=22)
       

