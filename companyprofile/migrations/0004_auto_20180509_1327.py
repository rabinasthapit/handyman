# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-09 07:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employeeprofile', '0010_cv'),
        ('companyprofile', '0003_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='cv',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employeeprofile.CV'),
        ),
        migrations.AlterField(
            model_name='application',
            name='vacancy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companyprofile.Vacancy'),
        ),
    ]
