# Generated by Django 2.0.2 on 2018-05-21 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0106_printorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='printorder',
            name='featured_provider_logo',
        ),
        migrations.RemoveField(
            model_name='printorder',
            name='isbn_download',
        ),
        migrations.DeleteModel(
            name='PrintOrder',
        ),
    ]
