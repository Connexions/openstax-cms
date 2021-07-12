# Generated by Django 3.2.4 on 2021-07-09 21:24

from django.db import migrations, models
import wagtail.search.index


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_delete_customizationformcontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='ErrataContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_state', models.CharField(choices=[('live', 'Live'), ('coming_soon', 'Coming soon'), ('new_edition_available', 'New edition available'), ('deprecated', 'Deprecated'), ('retired', 'Retired')], default='live', help_text='The state of the book.', max_length=255)),
                ('content', models.TextField()),
            ],
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
    ]
