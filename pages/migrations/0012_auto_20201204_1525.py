# Generated by Django 3.0.4 on 2020-12-04 21:25

from django.db import migrations
import pages.models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20201204_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutormarketing',
            name='features_cards',
            field=wagtail.fields.StreamField([('cards', wagtail.blocks.StructBlock([('icon', pages.models.APIImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(required=True)), ('description', wagtail.blocks.RichTextBlock(required=True))]))]),
        ),
    ]
