# Generated by Django 3.0.4 on 2020-09-28 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0052_pagelogentry'),
        ('global_settings', '0019_stickynote_show_popup'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiveToday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('give_link_text', models.CharField(max_length=255)),
                ('give_link', models.URLField(blank=True, help_text='URL to Rice Give page or something similar', verbose_name='Give link')),
                ('start', models.DateTimeField(help_text='Set the start date for Give Today to display', null=True)),
                ('expires', models.DateTimeField(help_text='Set the date to expire displaying Give Today', null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Give Today',
            },
        ),
    ]
