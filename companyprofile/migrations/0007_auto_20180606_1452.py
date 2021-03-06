# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-06 09:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companyprofile', '0006_auto_20180522_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='cv',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='employeeprofile.CV'),
        ),
        migrations.AlterField(
            model_name='application',
            name='vacancy',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='companyprofile.Vacancy'),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='companyprofile.Companyprofile'),
        ),
    ]
