# Generated by Django 2.0.13 on 2019-08-28 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesforce', '0019_adoptionopportunityrecord_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='salesforce_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
