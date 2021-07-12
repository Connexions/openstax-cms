# Generated by Django 3.2.4 on 2021-07-12 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0008_alter_erratacontent_book_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='erratacontent',
            name='book_state',
            field=models.CharField(choices=[('live', 'Live'), ('coming_soon', 'Coming soon'), ('new_edition_available', 'New edition available'), ('deprecated', 'Deprecated'), ('retired', 'Retired')], default='live', help_text='The state of the book.', max_length=255),
        ),
    ]
