# Generated by Django 3.0.4 on 2021-05-17 14:57

from django.db import migrations
import pages.custom_blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0044_auto_20210513_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutormarketing',
            name='feedback_video',
        ),
        migrations.AddField(
            model_name='tutormarketing',
            name='feedback_media',
            field=wagtail.core.fields.StreamField([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.custom_blocks.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))])), ('video', wagtail.core.blocks.RawHTMLBlock())], default=''),
            preserve_default=False,
        ),
    ]
