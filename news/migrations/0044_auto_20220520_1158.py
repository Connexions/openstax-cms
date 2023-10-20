# Generated by Django 3.2.5 on 2022-05-20 16:58

from django.db import migrations
import news.models
import wagtail.blocks
import wagtail.fields
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0043_alter_newsarticle_featured_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='body',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.blocks.StructBlock([('image', news.models.ImageChooserBlock()), ('caption', wagtail.blocks.RichTextBlock()), ('alignment', news.models.ImageFormatChoiceBlock()), ('alt_text', wagtail.blocks.CharBlock(required=False))], icon='image', label='Aligned image')), ('pullquote', wagtail.blocks.StructBlock([('quote', wagtail.blocks.TextBlock('quote title')), ('attribution', wagtail.blocks.CharBlock())])), ('aligned_html', wagtail.blocks.RawHTMLBlock(icon='code', label='Raw HTML')), ('document', news.models.BlogDocumentChooserBlock(icon='doc-full-inverse')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media', label='Embed Media URL')), ('blog_cta', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.TextBlock()), ('button_text', wagtail.blocks.CharBlock()), ('button_href', wagtail.blocks.URLBlock()), ('alignment', news.models.CTAAlignmentChoiceBlock())], icon='form', label='Call to Action block'))]),
        ),
        migrations.AlterField(
            model_name='pressrelease',
            name='body',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.blocks.StructBlock([('image', news.models.ImageChooserBlock()), ('caption', wagtail.blocks.RichTextBlock()), ('alignment', news.models.ImageFormatChoiceBlock()), ('alt_text', wagtail.blocks.CharBlock(required=False))], icon='image', label='Aligned image')), ('pullquote', wagtail.blocks.StructBlock([('quote', wagtail.blocks.TextBlock('quote title')), ('attribution', wagtail.blocks.CharBlock())])), ('aligned_html', wagtail.blocks.RawHTMLBlock(icon='code', label='Raw HTML')), ('document', news.models.BlogDocumentChooserBlock(icon='doc-full-inverse')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media', label='Embed Media URL')), ('blog_cta', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.TextBlock()), ('button_text', wagtail.blocks.CharBlock()), ('button_href', wagtail.blocks.URLBlock()), ('alignment', news.models.CTAAlignmentChoiceBlock())], icon='form', label='Call to Action block'))]),
        ),
    ]
