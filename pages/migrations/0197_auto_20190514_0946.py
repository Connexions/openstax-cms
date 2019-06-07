# Generated by Django 2.0.13 on 2019-05-14 14:46

from django.db import migrations
import pages.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0196_auto_20190513_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institutionalpartnerprogrampage',
            name='section_7_icons',
            field=wagtail.core.fields.StreamField([('card', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))])), ('image_alt_text', wagtail.core.blocks.CharBlock()), ('current_cohort', wagtail.core.blocks.BooleanBlock(required=False))])))]),
        ),
    ]
