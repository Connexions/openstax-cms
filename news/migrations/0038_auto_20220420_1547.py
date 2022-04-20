# Generated by Django 3.2.9 on 2022-04-20 20:47

from django.db import migrations
import news.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0037_newsarticle_collections'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='article_subjects',
            field=wagtail.core.fields.StreamField([('subject', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('subject', news.models.BlogCollectionChooserBlock(label='Blog Subject', required=True, target_model='snippets.Subject'))])))], null=True),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='collections',
            field=wagtail.core.fields.StreamField([('collection', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('collection', news.models.BlogCollectionChooserBlock(label='Blog Collection', required=True, target_model='snippets.BlogCollection')), ('featured', wagtail.core.blocks.BooleanBlock(label='Featured', required=False)), ('popular', wagtail.core.blocks.BooleanBlock(label='Popular', required=False))])))], null=True),
        ),
    ]
