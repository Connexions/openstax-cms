# Generated by Django 3.0.4 on 2020-09-28 19:05

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial_squashed_0232_auto_20200623_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='customer_service',
            field=wagtail.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='mailing_address',
            field=wagtail.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='mailing_header',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='tagline',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='erratalist',
            name='deprecated_errata_message',
            field=wagtail.fields.RichTextField(help_text='Errata message for deprecated books, controlled via the book state field.'),
        ),
        migrations.AlterField(
            model_name='erratalist',
            name='new_edition_errata_message',
            field=wagtail.fields.RichTextField(help_text='Errata message for books with new editions, controlled via the book state field.'),
        ),
        migrations.AlterField(
            model_name='giveform',
            name='page_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='adopt_cta',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='adopt_heading',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='get_started_step_1_cta',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='get_started_step_1_heading',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='get_started_step_2_heading',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='get_started_step_2_logged_in_cta',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='get_started_step_2_logged_out_cta',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='get_started_step_3_cta',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='get_started_step_3_heading',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='access_button_cta',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='access_button_link',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='access_tagline',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='floating_footer_button_1_caption',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='floating_footer_button_1_cta',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='floating_footer_button_1_link',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='floating_footer_button_2_caption',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='floating_footer_button_2_cta',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='floating_footer_button_2_link',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='icon_1_paragraph',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='icon_1_subheading',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='icon_2_paragraph',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='icon_2_subheading',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='icon_3_paragraph',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='icon_3_subheading',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='icon_4_paragraph',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='icon_4_subheading',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='pop_up_text',
            field=wagtail.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='section_4_coming_soon_heading',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='section_4_coming_soon_text',
            field=wagtail.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='section_4_paragraph',
            field=wagtail.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='section_4_resource_fine_print',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='section_5_science_heading',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='section_5_science_paragraph',
            field=wagtail.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='section_6_heading',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='section_6_knowledge_base_copy',
            field=wagtail.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='printorder',
            name='featured_provider_intro_blurb',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='printorder',
            name='other_providers_intro_blurb',
            field=models.TextField(),
        ),
    ]
