# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-08 08:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companyprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=30)),
                ('tag', models.CharField(max_length=30)),
                ('company', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='companyprofile.Companyprofile')),
            ],
        ),
    ]
