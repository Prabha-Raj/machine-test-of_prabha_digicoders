from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    dob=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    mobileno=models.CharField(max_length=20)
    password=models.CharField(max_length=50)
    collegename=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    emailaddress=models.CharField(max_length=50)
