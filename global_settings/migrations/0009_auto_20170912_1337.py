# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-12 18:37
from __future__ import unicode_literals

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('global_settings', '0008_auto_20170822_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='copyright',
            field=wagtail.fields.RichTextField(),
        ),
    ]
