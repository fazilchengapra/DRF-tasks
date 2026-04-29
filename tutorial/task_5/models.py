from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=25)
    price = models.IntegerField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    profile_pic = models.ImageField(upload_to='img')
    courses = models.ManyToManyField(Course)