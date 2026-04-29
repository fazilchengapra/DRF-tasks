from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
