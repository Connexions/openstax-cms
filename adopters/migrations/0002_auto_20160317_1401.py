# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-17 19:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adopters', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Adopters',
            new_name='Adopter',
        ),
    ]
