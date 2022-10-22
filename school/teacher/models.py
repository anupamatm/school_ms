from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length = 30)  # varchar(30)
    student_email = models.CharField(max_length = 30)    
    student_gender = models.CharField(max_length = 30)
    student_dob = models.CharField(max_length = 30)
    student_password = models.CharField(max_length = 30)
    student_phone = models.BigIntegerField()
    student_photo = models.ImageField(upload_to = 'student/')                     
    student_address = models.CharField(max_length = 60)
    student_parrent_name = models.CharField(max_length = 60)