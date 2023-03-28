# Generated by Django 4.0.8 on 2023-03-23 19:32

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0073_assignable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignable',
            name='admin_button_text',
        ),
        migrations.RemoveField(
            model_name='assignable',
            name='admin_link',
        ),
        migrations.RemoveField(
            model_name='assignable',
            name='admin_text',
        ),
        migrations.RemoveField(
            model_name='assignable',
            name='instructor_button_text',
        ),
        migrations.RemoveField(
            model_name='assignable',
            name='instructor_link',
        ),
        migrations.RemoveField(
            model_name='assignable',
            name='instructor_text',
        ),
        migrations.AddField(
            model_name='assignable',
            name='add_assignable_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assignable',
            name='add_assignable_header',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='assignable',
            name='add_assignable_html',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assignable',
            name='available_courses',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assignable',
            name='available_courses_header',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='assignable',
            name='courses_coming_soon_header',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
