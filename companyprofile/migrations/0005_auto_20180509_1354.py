# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-09 08:09
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companyprofile', '0004_auto_20180509_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=30),
        ),
    ]