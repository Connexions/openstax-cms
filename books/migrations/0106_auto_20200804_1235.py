# Generated by Django 3.0.4 on 2020-08-04 17:35

import books.models
from django.db import migrations
import snippets.models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0105_merge_20200727_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='give_today',
            field=wagtail.core.fields.StreamField([('content', books.models.GiveTodayChooserBlock(snippets.models.GiveToday))], blank=True, help_text='Give link text and url.', null=True),
        ),
    ]
