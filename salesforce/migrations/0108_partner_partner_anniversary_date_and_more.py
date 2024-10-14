# Generated by Django 5.1.1 on 2024-10-14 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("salesforce", "0107_alter_resourcedownload_account_uuid_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="partner",
            name="partner_anniversary_date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="partner",
            name="salesforce_created_date",
            field=models.DateTimeField(null=True),
        ),
        migrations.DeleteModel(
            name="PartnerReview",
        ),
    ]
