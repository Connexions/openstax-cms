# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 18:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import pages.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0030_index_on_pagerevision_created_at'),
        ('pages', '0068_auto_20161025_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro_heading', models.CharField(max_length=255)),
                ('intro_description', models.TextField()),
                ('row_1', wagtail.core.fields.StreamField((('column', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
