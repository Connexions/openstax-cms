# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-23 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0009_studentresource_unlocked_resource'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
