from django.db import models

# Create your models here
class Student1(models.Model):
    name = models.CharField(max_length=30)  # varchar(30)
    email = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    phone = models.BigIntegerField()