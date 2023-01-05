# Generated by Django 3.2.5 on 2022-06-16 18:58

from django.db import migrations
import news.models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('webinars', '0002_webinar_display_on_tutor_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='webinar',
            name='webinar_subjects',
            field=wagtail.fields.StreamField([('subject', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('subject', news.models.BlogCollectionChooserBlock(label='Blog Subject', required=True, target_model='snippets.Subject')), ('featured', wagtail.blocks.BooleanBlock(label='Featured', required=False))])))], blank=True, null=True),
        ),
    ]
