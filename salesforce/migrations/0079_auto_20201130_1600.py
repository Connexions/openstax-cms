# Generated by Django 3.0.4 on 2020-11-30 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesforce', '0078_auto_20201119_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnerreview',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Edited', 'Edited'), ('Awaiting Approval', 'Awaiting Approval'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Deleted', 'Deleted')], default='New', max_length=255),
        ),
    ]
