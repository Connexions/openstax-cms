# Generated by Django 3.2.9 on 2022-04-27 16:21

from django.db import migrations
import news.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0039_auto_20220427_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='content_types',
            field=wagtail.core.fields.StreamField([('content_type', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('content_type', news.models.ContentTypeChooserBlock(label='Blog Content Type', required=True, target_model='snippets.BlogContentType'))])))], null=True),
        ),
    ]
