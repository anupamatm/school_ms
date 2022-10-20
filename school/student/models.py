from django.db import models

# Create your models here.
class StudentLogin(models.Model):
    student_uid = models.CharField(max_length = 30)
    student_pwd = models.CharField(max_length = 30)