# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-12 13:42
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
        ('wagtailcore', '0028_merge'),
        ('pages', '0062_termsofservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='AP',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro_heading', models.CharField(max_length=255)),
                ('intro_description', models.TextField()),
                ('row_1', wagtail.core.fields.StreamField((('column', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),))),
                ('row_2', wagtail.core.fields.StreamField((('column', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
