# Generated by Django 3.2.9 on 2022-02-07 20:53

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0053_alter_supporters_funder_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supporters',
            name='funder_groups',
            field=wagtail.fields.StreamField([('content', wagtail.blocks.StructBlock([('group_title', wagtail.blocks.CharBlock(form_classname='name of funder group')), ('description', wagtail.blocks.TextBlock(form_classname='description of funder group')), ('funders', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('funder_name', wagtail.blocks.CharBlock(required=True)), ('url', wagtail.blocks.URLBlock(required=False))])))]))]),
        ),
    ]
