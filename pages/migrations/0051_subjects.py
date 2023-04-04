# Generated by Django 3.2.9 on 2022-02-01 15:43

from django.db import migrations, models
import django.db.models.deletion
import pages.custom_blocks
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('pages', '0050_auto_20211216_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('heading', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('tutor_ad', wagtail.fields.StreamField([('content', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock()), ('image', pages.custom_blocks.APIImageChooserBlock()), ('ad_html', wagtail.blocks.TextBlock()), ('link_text', wagtail.blocks.CharBlock()), ('link_href', wagtail.blocks.URLBlock())]))])),
                ('about_os', wagtail.fields.StreamField([('content', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock()), ('image', pages.custom_blocks.APIImageChooserBlock()), ('os_text', wagtail.blocks.TextBlock()), ('link_text', wagtail.blocks.CharBlock()), ('link_href', wagtail.blocks.URLBlock())]))])),
                ('info_boxes', wagtail.fields.StreamField([('info_box', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', pages.custom_blocks.APIImageChooserBlock()), ('heading', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.CharBlock())])))])),
                ('philanthropic_support', models.TextField(blank=True, null=True)),
                ('translations', wagtail.fields.StreamField([('translation', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('locale', wagtail.blocks.CharBlock()), ('slug', wagtail.blocks.CharBlock())])))], blank=True, null=True)),
                ('heading_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('promote_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'New Subjects Page',
            },
            bases=('wagtailcore.page',),
        ),
    ]
