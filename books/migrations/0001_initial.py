# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 21:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('wagtailimages', '0010_change_on_delete_behaviour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ally_category', models.CharField(choices=[('OH', 'Online Homework'), ('AC', 'Adaptive Courseware'), ('CT', 'Customized Tools')], max_length=2)),
                ('heading', models.CharField(max_length=255)),
                ('description', wagtail.wagtailcore.fields.RichTextField()),
                ('link_url', models.URLField(blank=True, help_text='Call to Action Link')),
                ('link_text', models.CharField(help_text='Call to Action Text', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('university', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('senior_author', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('revision', models.CharField(blank=True, max_length=255, null=True)),
                ('description', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('publish_date', models.DateField(blank=True, null=True)),
                ('isbn_10', models.IntegerField(blank=True, null=True)),
                ('isbn_13', models.CharField(blank=True, max_length=255, null=True)),
                ('cover_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BookIndex',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('page_description', wagtail.wagtailcore.fields.RichTextField()),
                ('dev_standards_heading', models.CharField(blank=True, max_length=255, null=True)),
                ('dev_standard_1_heading', models.CharField(blank=True, max_length=255, null=True)),
                ('dev_standard_1_description', wagtail.wagtailcore.fields.RichTextField()),
                ('dev_standard_2_heading', models.CharField(blank=True, max_length=255, null=True)),
                ('dev_standard_2_description', wagtail.wagtailcore.fields.RichTextField()),
                ('dev_standard_3_heading', models.CharField(blank=True, max_length=255, null=True)),
                ('dev_standard_3_description', wagtail.wagtailcore.fields.RichTextField()),
                ('subject_list_heading', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='FacultyResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255)),
                ('description', wagtail.wagtailcore.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_text', wagtail.wagtailcore.fields.RichTextField()),
                ('quote_author', models.CharField(max_length=255)),
                ('quote_author_school', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StudentResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255)),
                ('description', wagtail.wagtailcore.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='BookAllies',
            fields=[
                ('allies_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.Allies')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('ally', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_allies', to='books.Book')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=('books.allies', models.Model),
        ),
        migrations.CreateModel(
            name='BookFacultyResources',
            fields=[
                ('facultyresources_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.FacultyResources')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('resource', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_faculty_resources', to='books.Book')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=('books.facultyresources', models.Model),
        ),
        migrations.CreateModel(
            name='BookQuotes',
            fields=[
                ('quotes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.Quotes')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('ally', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_quotes', to='books.Book')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=('books.quotes', models.Model),
        ),
        migrations.CreateModel(
            name='BookStudentResources',
            fields=[
                ('studentresources_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.StudentResources')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('resource', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_student_resources', to='books.Book')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=('books.studentresources', models.Model),
        ),
        migrations.CreateModel(
            name='ContributingAuthors',
            fields=[
                ('authors_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.Authors')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('resource', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_contributing_authors', to='books.Book')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=('books.authors', models.Model),
        ),
        migrations.AddField(
            model_name='allies',
            name='logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
