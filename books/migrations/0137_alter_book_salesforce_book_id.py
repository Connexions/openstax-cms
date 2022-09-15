# Generated by Django 3.2.5 on 2022-09-15 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0136_auto_20220915_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='salesforce_book_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Salesforce book id (No tracking and not included on adoption or interest form if left blank)'),
        ),
    ]
