# Generated by Django 2.0.2 on 2018-03-01 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allies', '0010_ally_do_not_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allysubject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='snippets.Subject'),
        ),
    ]
