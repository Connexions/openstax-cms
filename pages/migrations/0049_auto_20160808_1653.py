# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-08 21:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0048_auto_20160808_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='openstaxteam',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='openstaxteam',
            name='link_external',
        ),
        migrations.RemoveField(
            model_name='openstaxteam',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='strategicadvisors',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='strategicadvisors',
            name='link_external',
        ),
        migrations.RemoveField(
            model_name='strategicadvisors',
            name='link_page',
        ),
    ]
