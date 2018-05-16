# Generated by Django 2.0.2 on 2018-05-15 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_squashed_0028_remove_pressindex_news_mentions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='author',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='heading',
            field=models.CharField(help_text='Heading displayed on website', max_length=250),
        ),
        migrations.AlterField(
            model_name='pressindex',
            name='experts_blurb',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='pressindex',
            name='experts_heading',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pressindex',
            name='press_inquiry_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='pressindex',
            name='press_inquiry_phone',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pressrelease',
            name='excerpt',
            field=models.CharField(max_length=255),
        ),
    ]
