# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20160526_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='highereducation',
            name='row_0_box_1_content',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='highereducation',
            name='row_0_box_1_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='highereducation',
            name='row_0_box_2_content',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='highereducation',
            name='row_0_box_2_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='highereducation',
            name='row_0_box_3_content',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='highereducation',
            name='row_0_box_3_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
