# Generated by Django 2.0.2 on 2018-07-25 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0130_group_openstaxpeople'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teampage',
            name='people',
        ),
    ]
