# Generated by Django 4.1.2 on 2022-11-03 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('dob', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('phone', models.BigIntegerField()),
            ],
        ),
    ]
