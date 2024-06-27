# Generated by Django 5.0.4 on 2024-06-27 23:30

import django.db.models.deletion
import pages.custom_blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0083_alter_k12mainpage_testimonials"),
        ("wagtailcore", "0093_uploadedfile"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomizablePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            (
                                "hero",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("heading", wagtail.blocks.CharBlock(required=True)),
                                        ("sub_heading", wagtail.blocks.CharBlock(required=False)),
                                        ("description", wagtail.blocks.RichTextBlock(required=False)),
                                        ("image", wagtail.images.blocks.ImageChooserBlock(required=False)),
                                        ("primary_cta_text", wagtail.blocks.CharBlock(required=False)),
                                        ("primary_cta_link", wagtail.blocks.URLBlock(required=False)),
                                        ("secondary_cta_text", wagtail.blocks.CharBlock(required=False)),
                                        ("secondary_cta_link", wagtail.blocks.URLBlock(required=False)),
                                    ]
                                ),
                            ),
                            (
                                "section",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("heading", wagtail.blocks.CharBlock(required=False)),
                                        ("html", wagtail.blocks.RawHTMLBlock(required=False)),
                                        (
                                            "cards",
                                            wagtail.blocks.ListBlock(
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "style",
                                                            wagtail.blocks.ChoiceBlock(
                                                                choices=[("rounded", "Rounded"), ("square", "Square")]
                                                            ),
                                                        ),
                                                        ("heading", wagtail.blocks.CharBlock(required=True)),
                                                        ("description", wagtail.blocks.RichTextBlock(required=True)),
                                                        ("link", wagtail.blocks.URLBlock(required=False)),
                                                        ("cta", wagtail.blocks.CharBlock(required=False)),
                                                        (
                                                            "image",
                                                            wagtail.images.blocks.ImageChooserBlock(required=False),
                                                        ),
                                                    ],
                                                    required=False,
                                                )
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            ("paragraph", wagtail.blocks.RichTextBlock()),
                            ("image", pages.custom_blocks.APIImageChooserBlock()),
                            ("html", wagtail.blocks.RawHTMLBlock()),
                        ]
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
