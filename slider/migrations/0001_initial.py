# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-20 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='slider/', verbose_name='upload image of 1697 x 650')),
            ],
        ),
    ]
