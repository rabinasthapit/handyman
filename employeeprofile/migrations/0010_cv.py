# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-09 07:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employeeprofile', '0009_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('cv_file', models.FileField(upload_to='cv/')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeprofile.EmployeeProfile')),
            ],
        ),
    ]
