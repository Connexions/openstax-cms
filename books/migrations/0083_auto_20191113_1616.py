# Generated by Django 2.2.5 on 2019-11-13 22:16

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0082_book_videos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='videos',
            field=wagtail.core.fields.StreamField([('video', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.RichTextBlock()), ('embed', wagtail.core.blocks.RawHTMLBlock())])))], blank=True, null=True),
        ),
    ]
