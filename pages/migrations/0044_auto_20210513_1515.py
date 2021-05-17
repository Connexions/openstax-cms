# Generated by Django 3.0.4 on 2021-05-13 20:15

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0043_auto_20210506_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutormarketing',
            name='feedback_image',
        ),
        migrations.AddField(
            model_name='tutormarketing',
            name='feedback_video',
            field=wagtail.core.fields.StreamField([('html', wagtail.core.blocks.RawHTMLBlock())], default=''),
            preserve_default=False,
        ),
    ]
