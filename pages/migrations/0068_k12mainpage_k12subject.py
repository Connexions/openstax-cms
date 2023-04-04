# Generated by Django 3.2.16 on 2023-01-12 20:26

from django.db import migrations, models
import django.db.models.deletion
import pages.custom_blocks
import wagtail.blocks
import wagtail.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('pages', '0067_learningresearchpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='K12Subject',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('subheader', models.TextField(default='HIGH SCHOOL')),
                ('books_heading', models.TextField(default='')),
                ('books_short_desc', wagtail.fields.RichTextField(default='')),
                ('about_books_heading', models.TextField(default='About the Books')),
                ('about_books_text', models.CharField(blank=True, default='FIND SUPPLEMENTAL RESOURCES', max_length=255)),
                ('adoption_heading', models.TextField(default='Using an OpenStax resource in your classroom? Let us know!')),
                ('adoption_text', wagtail.fields.RichTextField(default="<p>Help us continue to make high-quality educational materials accessible by letting us know you've adopted! Our future grant funding is based on educator adoptions and the number of students we impact.</p>")),
                ('adoption_link_text', models.CharField(default='Report Your Adoption', max_length=255)),
                ('adoption_link', models.URLField(blank=True, default='/adoption')),
                ('quote_heading', models.TextField(blank=True, default='What Our Teachers Say')),
                ('quote_text', models.CharField(blank=True, default='', max_length=255)),
                ('resources_heading', models.TextField(default='Supplemental Resources')),
                ('blogs_heading', models.TextField(blank=True, default='Blogs for High School Teachers')),
                ('rfi_heading', models.TextField(default="Don't see what you're looking for?")),
                ('rfi_text', models.CharField(default="We're here to answer any questions you may have. Complete the form to get in contact with a member of our team.", max_length=255)),
                ('promote_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'K12 Subject',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='K12MainPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('banner_headline', models.CharField(blank=True, default='', max_length=255)),
                ('banner_description', models.TextField(blank=True, default='')),
                ('features_cards', wagtail.fields.StreamField([('features_cards', wagtail.blocks.StructBlock([('icon', pages.custom_blocks.APIImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(required=True)), ('description', wagtail.blocks.RichTextBlock(required=True))]))])),
                ('highlights_header', wagtail.fields.RichTextField(blank=True, default='')),
                ('highlights', wagtail.fields.StreamField([('highlight', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('highlight_subheader', wagtail.blocks.TextBlock(required=False)), ('highlight_text', wagtail.blocks.CharBlock(Required=False))])))])),
                ('stats_grid', wagtail.fields.StreamField([('stat', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('bold_stat_text', wagtail.blocks.TextBlock(required=False)), ('normal_stat_text', wagtail.blocks.CharBlock(required=False))])))])),
                ('subject_library_header', models.CharField(blank=True, default='', max_length=255)),
                ('subject_library_description', models.TextField(blank=True, default='')),
                ('testimonials_header', models.CharField(blank=True, default='', max_length=255)),
                ('testimonials_description', models.TextField(blank=True, default='')),
                ('testimonials', wagtail.fields.StreamField([('testimonials', wagtail.blocks.StructBlock([('author_icon', pages.custom_blocks.APIImageChooserBlock(required=False)), ('author', wagtail.blocks.CharBlock(required=True)), ('testimonial', wagtail.blocks.RichTextBlock(required=True))]))])),
                ('faq_header', models.CharField(blank=True, default='', max_length=255)),
                ('faqs', wagtail.fields.StreamField([('faq', wagtail.blocks.StructBlock([('question', wagtail.blocks.RichTextBlock(required=True)), ('slug', wagtail.blocks.CharBlock(required=True)), ('answer', wagtail.blocks.RichTextBlock(required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False))]))])),
                ('rfi_header', models.CharField(blank=True, default='', max_length=255)),
                ('rfi_description', models.TextField(blank=True, default='')),
                ('sticky_header', models.CharField(blank=True, default='', max_length=255)),
                ('sticky_description', models.TextField(blank=True, default='')),
                ('banner_right_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('highlights_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('promote_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('rfi_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('stats_image1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('stats_image2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('stats_image3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'K12 Main Page',
            },
            bases=('wagtailcore.page',),
        ),
    ]
