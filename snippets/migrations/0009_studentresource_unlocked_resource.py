# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-12 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0008_auto_20170427_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentresource',
            name='unlocked_resource',
            field=models.BooleanField(default=True),
        ),
    ]
