# Generated by Django 2.2.5 on 2019-10-08 20:46

from django.db import migrations
import news.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0033_auto_20181113_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock([('image', news.models.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock()), ('alignment', news.models.ImageFormatChoiceBlock()), ('alt_text', wagtail.core.blocks.CharBlock(required=False))], icon='image', label='Aligned image')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', news.models.HTMLAlignmentChoiceBlock())], icon='code', label='Raw HTML')), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media', label='Embed Media URL'))]),
        ),
        migrations.AlterField(
            model_name='pressrelease',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock([('image', news.models.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock()), ('alignment', news.models.ImageFormatChoiceBlock()), ('alt_text', wagtail.core.blocks.CharBlock(required=False))], icon='image', label='Aligned image')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', news.models.HTMLAlignmentChoiceBlock())], icon='code', label='Raw HTML')), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media', label='Embed Media URL'))]),
        ),
    ]
