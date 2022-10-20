from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_name = models.CharField(max_length = 30)  # varchar(30)
    teacher_email = models.CharField(max_length = 30)
    qualifiaction = models.CharField(max_length = 30)
    exp = models.IntegerField()
    gender = models.CharField(max_length = 30)
    teacher_dob = models.CharField(max_length = 30)
    teacher_password = models.CharField(max_length = 30)
    teacher_phone = models.BigIntegerField()
    teacher_photo = models.ImageField(upload_to = 'teacher/')                     
    teacher_address = models.CharField(max_length = 60)


class AdminLogin(models.Model):
    admin_uid = models.CharField(max_length = 30)
    admin_pwd = models.CharField(max_length = 30)