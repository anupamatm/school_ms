# Generated by Django 4.1.2 on 2022-10-24 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school_admin', '0003_adminlogin'),
        ('teacher', '0002_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('student_email', models.CharField(max_length=30)),
                ('student_gender', models.CharField(max_length=30)),
                ('student_dob', models.CharField(max_length=30)),
                ('student_password', models.CharField(max_length=30)),
                ('student_phone', models.BigIntegerField()),
                ('student_photo', models.ImageField(upload_to='student/')),
                ('student_address', models.CharField(max_length=60)),
                ('student_parrent_name', models.CharField(max_length=60)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_admin.teacher')),
            ],
        ),
    ]