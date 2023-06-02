# Generated by Django 4.0.8 on 2023-06-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0146_alter_facultyresources_link_external_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultyresources',
            name='link_external',
            field=models.URLField(blank=True, default='', help_text='Provide an external URL starting with https:// (or fill out either one of the following two).', verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='studentresources',
            name='link_external',
            field=models.URLField(blank=True, default='', help_text='Provide an external URL starting with http:// (or fill out either one of the following two).', verbose_name='External link'),
        ),
    ]
