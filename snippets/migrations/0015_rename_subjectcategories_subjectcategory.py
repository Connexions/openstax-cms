# Generated by Django 3.2.9 on 2022-01-27 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('snippets', '0014_auto_20220126_1603'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubjectCategories',
            new_name='SubjectCategory',
        ),
    ]
