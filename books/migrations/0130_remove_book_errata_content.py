# Generated by Django 3.2.4 on 2021-07-12 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0129_auto_20210709_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='errata_content',
        ),
    ]
