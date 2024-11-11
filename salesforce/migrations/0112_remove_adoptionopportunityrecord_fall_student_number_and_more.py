# Generated by Django 5.1.1 on 2024-10-17 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("salesforce", "0111_alter_partner_partner_sf_account_id_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="adoptionopportunityrecord",
            name="fall_student_number",
        ),
        migrations.RemoveField(
            model_name="adoptionopportunityrecord",
            name="spring_student_number",
        ),
        migrations.RemoveField(
            model_name="adoptionopportunityrecord",
            name="summer_student_number",
        ),
        migrations.AddField(
            model_name="adoptionopportunityrecord",
            name="adoption_type",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="adoptionopportunityrecord",
            name="base_year",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="adoptionopportunityrecord",
            name="confirmation_date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="adoptionopportunityrecord",
            name="confirmation_type",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="adoptionopportunityrecord",
            name="how_using",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="adoptionopportunityrecord",
            name="opportunity_stage",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="adoptionopportunityrecord",
            name="savings",
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name="adoptionopportunityrecord",
            name="students",
            field=models.IntegerField(null=True),
        ),
    ]
