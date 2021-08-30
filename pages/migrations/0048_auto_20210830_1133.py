# Generated by Django 3.2.4 on 2021-08-30 16:33

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0047_institutionalpartnership_application_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='erratalist',
            name='about_header',
            field=models.CharField(default='About our correction schedule', help_text='About our correction schedule', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='erratalist',
            name='about_popup',
            field=wagtail.core.fields.RichTextField(default='Errata received from March through...', help_text='Instructor and student resources..." the stuff that will be in the popup'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='erratalist',
            name='about_text',
            field=wagtail.core.fields.RichTextField(default='Instructor and student resources...', help_text='Errata received from March through..." the stuff that will show on the page'),
            preserve_default=False,
        ),
    ]
