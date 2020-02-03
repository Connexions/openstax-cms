# Generated by Django 2.2.8 on 2020-02-03 15:54

from django.db import migrations
import pages.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0220_auto_20200121_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roverpage',
            name='office_hours',
            field=wagtail.core.fields.StreamField([('content', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.RichTextBlock()), ('more_info', wagtail.core.blocks.RichTextBlock()), ('image', pages.models.APIImageChooserBlock()), ('link_url', wagtail.core.blocks.URLBlock()), ('link_text', wagtail.core.blocks.CharBlock())])))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='roverpage',
            name='section_5',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('blurb', wagtail.core.blocks.TextBlock()), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('video', wagtail.core.blocks.RawHTMLBlock()), ('heading', wagtail.core.blocks.CharBlock()), ('blurb', wagtail.core.blocks.TextBlock())]))), ('nav_text', wagtail.core.blocks.CharBlock(required=False)), ('see_more_text', wagtail.core.blocks.CharBlock(required=False)), ('see_more_url', wagtail.core.blocks.URLBlock(required=False))], blank=True, null=True),
        ),
    ]
