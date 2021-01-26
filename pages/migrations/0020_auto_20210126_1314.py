# Generated by Django 3.0.4 on 2021-01-26 19:14

from django.db import migrations
import pages.custom_blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_auto_20210126_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impact',
            name='improving_access',
            field=wagtail.core.fields.StreamField([('content', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.custom_blocks.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))])), ('heading', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.RichTextBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_href', wagtail.core.blocks.URLBlock())], max_num=1), blank=True))]),
        ),
    ]
