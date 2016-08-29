# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-29 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import pages.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('pages', '0054_auto_20160822_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('link', models.URLField()),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
        ),
        migrations.CreateModel(
            name='OurImpact',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro_heading', models.CharField(max_length=255)),
                ('intro_description', models.TextField()),
                ('row_1', wagtail.wagtailcore.fields.StreamField((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='OurImpactInstitutions',
            fields=[
                ('funder_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Funder')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='institutions', to='pages.OurImpact')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=('pages.funder', models.Model),
        ),
    ]
