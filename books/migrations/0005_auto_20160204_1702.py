# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20160204_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='authors',
            name='university',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
