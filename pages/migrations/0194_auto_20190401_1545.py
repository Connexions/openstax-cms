# Generated by Django 2.0.13 on 2019-04-01 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('pages', '0193_institutionalpartnerprogrampage_section_4_quote_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='institutionalpartnerprogrampage',
            name='section_1_background_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='institutionalpartnerprogrampage',
            name='section_5_image_caption',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
