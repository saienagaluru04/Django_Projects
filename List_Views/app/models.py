from django.db import models

# Create your models here.

class School(models.Model):
    scname = models.CharField(max_length=100)
    sclocation = models.CharField(max_length=100)
    scprincipal = models.CharField(max_length=100)

class Student(models.Model):
    scname = models.ForeignKey(School,on_delete=models.CASCADE)
    stname = models.CharField(max_length=100)
    stage  = models.IntegerField()
    