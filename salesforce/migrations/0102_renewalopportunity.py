# Generated by Django 3.2.5 on 2022-05-11 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesforce', '0101_merge_20220506_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='RenewalOpportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opportunity_id', models.CharField(max_length=255, unique=True)),
                ('account_uuid', models.UUIDField(null=True)),
                ('book_name', models.CharField(max_length=255)),
                ('fall_student_number', models.CharField(max_length=255)),
                ('spring_student_number', models.CharField(max_length=255)),
                ('renewal_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
