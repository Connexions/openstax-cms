# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='k12',
            name='allies_description',
        ),
        migrations.RemoveField(
            model_name='k12',
            name='allies_heading',
        ),
        migrations.RemoveField(
            model_name='k12',
            name='cnx_description',
        ),
        migrations.RemoveField(
            model_name='k12',
            name='cnx_heading',
        ),
        migrations.RemoveField(
            model_name='k12',
            name='k12_description',
        ),
        migrations.RemoveField(
            model_name='k12',
            name='k12_heading',
        ),
        migrations.RemoveField(
            model_name='k12',
            name='tutor_description',
        ),
        migrations.RemoveField(
            model_name='k12',
            name='tutor_heading',
        ),
        migrations.AddField(
            model_name='k12',
            name='box_1_description',
            field=wagtail.core.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='k12',
            name='box_1_heading',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='k12',
            name='box_2_description',
            field=wagtail.core.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='k12',
            name='box_2_heading',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='k12',
            name='box_3_description',
            field=wagtail.core.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='k12',
            name='box_3_heading',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='k12',
            name='box_4_description',
            field=wagtail.core.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='k12',
            name='box_4_heading',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='k12',
            name='box_5_description',
            field=wagtail.core.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='k12',
            name='box_5_heading',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='k12',
            name='description',
            field=wagtail.core.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='k12',
            name='heading',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
