# Generated by Django 4.1.2 on 2022-11-03 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_photo',
        ),
    ]
