# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20160527_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutusfunders',
            name='funders_ptr',
        ),
        migrations.RemoveField(
            model_name='aboutusfunders',
            name='page',
        ),
        migrations.RemoveField(
            model_name='funders',
            name='image',
        ),
        migrations.RemoveField(
            model_name='funders',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='funders',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='funder_intro',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='openstax_team_intro',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='strategic_advisors_intro',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='who_we_are',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='intro_heading',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutus',
            name='intro_paragraph',
            field=wagtail.wagtailcore.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutus',
            name='our_team_heading',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutus',
            name='tagline',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AboutUsFunders',
        ),
        migrations.DeleteModel(
            name='Funders',
        ),
    ]
