# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-04 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blog/'),
        ),
    ]