# Generated by Django 2.2.5 on 2019-10-14 19:37

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0080_merge_20191003_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='table_of_contents',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, editable=False, help_text='TOC.', null=True),
        ),
    ]
