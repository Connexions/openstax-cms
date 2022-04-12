# Generated by Django 3.2.9 on 2022-04-12 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0059_alter_supporters_funder_groups'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='whats_openstax_donate_text',
            new_name='whats_openstax_interest_text',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='whats_openstax_give_link',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='whats_openstax_give_text',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='whats_openstax_learn_more_link',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='whats_openstax_learn_more_text',
        ),
        migrations.AddField(
            model_name='homepage',
            name='map_button_text',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='map_text',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='homepage',
            name='whats_openstax_interest_headline',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='whats_openstax_interest_link_text',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
