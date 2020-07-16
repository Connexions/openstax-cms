# Generated by Django 3.0.4 on 2020-07-16 20:53

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0022_subject_page_content'),
        ('wagtaildocs', '0010_document_file_hash'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('books', '0100_videofacultyresources'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrientationFacultyResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_external', models.URLField(blank=True, help_text='Provide an external URL starting with https:// (or fill out either one of the following two).', verbose_name='External link')),
                ('link_text', models.CharField(help_text='Call to Action Text', max_length=255)),
                ('video_reference_number', models.IntegerField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, help_text='Late date resource was updated', null=True)),
                ('featured', models.BooleanField(default=False, help_text='Add to featured bar on resource page')),
                ('link_document', models.ForeignKey(blank=True, help_text='Or select a document for viewers to download.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(blank=True, help_text='Or select an existing page to attach.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('resource', models.ForeignKey(help_text='Manage resources through snippets.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='snippets.FacultyResource')),
            ],
        ),
        migrations.AlterField(
            model_name='facultyresources',
            name='link_external',
            field=models.URLField(blank=True, help_text='Provide an external URL starting with https:// (or fill out either one of the following two).', verbose_name='External link'),
        ),
        migrations.CreateModel(
            name='OrientationFacultyResources',
            fields=[
                ('orientationfacultyresource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.OrientationFacultyResource')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('book_orientation_faculty_resource', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_orientation_faculty_resources', to='books.Book')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('books.orientationfacultyresource', models.Model),
        ),
    ]
