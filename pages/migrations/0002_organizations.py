# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-16 17:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salesforce_id', models.CharField(max_length=255)),
                ('organization_name', models.CharField(max_length=255)),
                ('description',
                 wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('website', models.URLField(max_length=255, null=True)),
                ('page', modelcluster.fields.ParentalKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name='organizations', to='pages.Adopters')),
            ],
        ),
    ]
