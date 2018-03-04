# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-19 16:07
from __future__ import unicode_literals

from django.db import migrations
import pages.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0030_auto_20160719_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalpage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('tagline', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('list', wagtail.core.blocks.StreamBlock((('list_item', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=True)), ('description', wagtail.core.blocks.RichTextBlock()), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),), icon='list-ul')), ('two_columns', wagtail.core.blocks.StructBlock((('left_column', wagtail.core.blocks.StreamBlock((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())))), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('cta', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.URLBlock()), ('quote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.CharBlock()), ('author', wagtail.core.blocks.CharBlock()))))), icon='arrow-left', label='Left column content')), ('right_column', wagtail.core.blocks.StreamBlock((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())))), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('cta', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.URLBlock()), ('quote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.CharBlock()), ('author', wagtail.core.blocks.CharBlock()))))), icon='arrow-right', label='Right column content'))))), ('three_columns', wagtail.core.blocks.StructBlock((('left_column', wagtail.core.blocks.StreamBlock((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())))), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('cta', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.URLBlock()), ('quote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.CharBlock()), ('author', wagtail.core.blocks.CharBlock()))))), icon='arrow-left', label='Left column content')), ('center_column', wagtail.core.blocks.StreamBlock((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())))), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('cta', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.URLBlock()), ('quote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.CharBlock()), ('author', wagtail.core.blocks.CharBlock()))))), icon='arrow-up', label='Center column content')), ('right_column', wagtail.core.blocks.StreamBlock((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())))), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('cta', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.URLBlock()), ('quote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.CharBlock()), ('author', wagtail.core.blocks.CharBlock()))))), icon='arrow-right', label='Right column content'))))), ('person', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(required=True)), ('position', wagtail.core.blocks.CharBlock(required=True)), ('photo', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())))), ('biography', wagtail.core.blocks.RichTextBlock())))), ('html', wagtail.core.blocks.RawHTMLBlock()), ('content_row', wagtail.core.blocks.StreamBlock((('content_block', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('hidden', wagtail.core.blocks.BooleanBlock(required=False))))), ('quote_block', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.CharBlock()), ('author', wagtail.core.blocks.CharBlock()))))), icon='form')))),
        ),
    ]
