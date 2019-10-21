# Generated by Django 2.2.5 on 2019-10-21 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('pages', '0214_creatorfestpage_banner_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rovercardssection2',
            name='card_ptr',
        ),
        migrations.RemoveField(
            model_name='rovercardssection2',
            name='rover_cards',
        ),
        migrations.RemoveField(
            model_name='rovercardssection3',
            name='card_ptr',
        ),
        migrations.RemoveField(
            model_name='rovercardssection3',
            name='rover_cards',
        ),
        migrations.DeleteModel(
            name='Rover',
        ),
        migrations.DeleteModel(
            name='RoverCardsSection2',
        ),
        migrations.DeleteModel(
            name='RoverCardsSection3',
        ),
    ]
