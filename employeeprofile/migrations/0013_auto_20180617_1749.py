# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-17 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employeeprofile', '0012_auto_20180605_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degree',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employeeprofile.EmployeeProfile'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employeeprofile.EmployeeProfile'),
        ),
    ]
