# Generated by Django 3.0.4 on 2021-01-27 19:56

from django.db import migrations
import pages.custom_blocks
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0032_auto_20210127_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impact',
            name='making_a_difference',
            field=wagtail.fields.StreamField([('content', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.RichTextBlock()), ('stories', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', pages.custom_blocks.APIImageChooserBlock(required=False)), ('story_text', wagtail.blocks.TextBlock(required=False)), ('embedded_video', wagtail.blocks.RawHTMLBlock(required=False))])))]))]),
        ),
    ]
