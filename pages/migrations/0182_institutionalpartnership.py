# Generated by Django 2.0.9 on 2019-02-07 19:20

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailimages', '0001_squashed_0021'),
        ('pages', '0181_auto_20190118_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstitutionalPartnership',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading_year', models.CharField(max_length=255)),
                ('heading', models.CharField(max_length=255)),
                ('program_heading', models.CharField(max_length=255)),
                ('program_details', models.TextField()),
                ('cost_heading', models.CharField(max_length=255)),
                ('cost_details', models.TextField()),
                ('timeline_heading', models.CharField(max_length=255)),
                ('timeline_details', models.TextField()),
                ('what_you_get_heading', models.CharField(max_length=255)),
                ('what_you_get_details', models.TextField()),
                ('current_partners_heading', models.CharField(max_length=255)),
                ('current_partners_details', wagtail.core.fields.RichTextField()),
                ('quote', models.TextField()),
                ('quote_author', models.CharField(max_length=255)),
                ('quote_title', models.CharField(blank=True, max_length=255, null=True)),
                ('quote_school', models.CharField(blank=True, max_length=255, null=True)),
                ('application_heading', models.CharField(blank=True, max_length=255, null=True)),
                ('heading_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
