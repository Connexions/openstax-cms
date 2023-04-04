# Generated by Django 3.0.4 on 2020-12-04 21:20

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20201204_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutormarketing',
            name='cost_cards',
            field=wagtail.fields.StreamField([('cards', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('description', wagtail.blocks.RichTextBlock(required=True))]))]),
        ),
    ]
