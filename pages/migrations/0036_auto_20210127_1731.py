# Generated by Django 3.0.4 on 2021-01-27 23:31

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0035_auto_20210127_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impact',
            name='giving',
            field=wagtail.fields.StreamField([('content', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.TextBlock()), ('link_text', wagtail.blocks.CharBlock()), ('link_href', wagtail.blocks.URLBlock()), ('nonprofit_statement', wagtail.blocks.TextBlock()), ('annual_report_link_text', wagtail.blocks.CharBlock()), ('annual_report_link_href', wagtail.blocks.URLBlock())]))]),
        ),
    ]
