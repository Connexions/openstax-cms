# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-19 17:06
from __future__ import unicode_literals

from django.db import migrations
import pages.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0032_auto_20160719_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalpage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('tagline', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('multicolumn', wagtail.core.blocks.StreamBlock((('column', wagtail.core.blocks.StructBlock((('column', wagtail.core.blocks.StreamBlock((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())))), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('cta', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.URLBlock()), ('quote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.CharBlock()), ('author', wagtail.core.blocks.CharBlock())))), ('hide', wagtail.core.blocks.BooleanBlock())), icon='placeholder', label='Column content')),))),), icon='placeholder')), ('person', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(required=True)), ('position', wagtail.core.blocks.CharBlock(required=True)), ('photo', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())))), ('biography', wagtail.core.blocks.RichTextBlock())))), ('html', wagtail.core.blocks.RawHTMLBlock()))),
        ),
    ]
