# Generated by Django 5.0.4 on 2024-06-28 17:37

import pages.custom_blocks
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0087_alter_rootpage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rootpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "hero",
                        wagtail.blocks.StructBlock(
                            [
                                ("heading", wagtail.blocks.CharBlock(required=True)),
                                ("sub_heading", wagtail.blocks.CharBlock(required=False)),
                                ("description", pages.custom_blocks.APIRichTextBlock(required=False)),
                                (
                                    "image",
                                    wagtail.blocks.StructBlock(
                                        [
                                            ("image", wagtail.images.blocks.ImageChooserBlock(required=False)),
                                            ("alt_text", wagtail.blocks.CharBlock(required=False)),
                                            ("link", wagtail.blocks.URLBlock(required=False)),
                                            ("alignment", pages.custom_blocks.ImageFormatChoiceBlock(required=False)),
                                            (
                                                "identifier",
                                                wagtail.blocks.CharBlock(
                                                    help_text="Used by the frontend for Google Analytics.",
                                                    required=False,
                                                ),
                                            ),
                                        ],
                                        required=False,
                                    ),
                                ),
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
                                (
                                    "content",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StreamBlock(
                                            [
                                                (
                                                    "cards",
                                                    wagtail.blocks.ListBlock(
                                                        wagtail.blocks.StructBlock(
                                                            [
                                                                (
                                                                    "style",
                                                                    wagtail.blocks.ChoiceBlock(
                                                                        choices=[
                                                                            ("rounded", "Rounded"),
                                                                            ("square", "Square"),
                                                                        ]
                                                                    ),
                                                                ),
                                                                ("heading", wagtail.blocks.CharBlock(required=True)),
                                                                (
                                                                    "description",
                                                                    pages.custom_blocks.APIRichTextBlock(required=True),
                                                                ),
                                                                ("link", wagtail.blocks.URLBlock(required=False)),
                                                                ("cta", wagtail.blocks.CharBlock(required=False)),
                                                                (
                                                                    "image",
                                                                    wagtail.blocks.StructBlock(
                                                                        [
                                                                            (
                                                                                "image",
                                                                                wagtail.images.blocks.ImageChooserBlock(
                                                                                    required=False
                                                                                ),
                                                                            ),
                                                                            (
                                                                                "alt_text",
                                                                                wagtail.blocks.CharBlock(
                                                                                    required=False
                                                                                ),
                                                                            ),
                                                                            (
                                                                                "link",
                                                                                wagtail.blocks.URLBlock(required=False),
                                                                            ),
                                                                            (
                                                                                "alignment",
                                                                                pages.custom_blocks.ImageFormatChoiceBlock(
                                                                                    required=False
                                                                                ),
                                                                            ),
                                                                            (
                                                                                "identifier",
                                                                                wagtail.blocks.CharBlock(
                                                                                    help_text="Used by the frontend for Google Analytics.",
                                                                                    required=False,
                                                                                ),
                                                                            ),
                                                                        ],
                                                                        required=False,
                                                                    ),
                                                                ),
                                                            ],
                                                            required=False,
                                                        )
                                                    ),
                                                ),
                                                ("paragraph", pages.custom_blocks.APIRichTextBlock(required=False)),
                                                ("html", wagtail.blocks.RawHTMLBlock(required=False)),
                                                (
                                                    "image",
                                                    wagtail.blocks.StructBlock(
                                                        [
                                                            (
                                                                "image",
                                                                wagtail.images.blocks.ImageChooserBlock(required=False),
                                                            ),
                                                            ("alt_text", wagtail.blocks.CharBlock(required=False)),
                                                            ("link", wagtail.blocks.URLBlock(required=False)),
                                                            (
                                                                "alignment",
                                                                pages.custom_blocks.ImageFormatChoiceBlock(
                                                                    required=False
                                                                ),
                                                            ),
                                                            (
                                                                "identifier",
                                                                wagtail.blocks.CharBlock(
                                                                    help_text="Used by the frontend for Google Analytics.",
                                                                    required=False,
                                                                ),
                                                            ),
                                                        ],
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "faqs",
                                                    wagtail.blocks.ListBlock(
                                                        wagtail.blocks.StructBlock(
                                                            [
                                                                (
                                                                    "question",
                                                                    wagtail.blocks.RichTextBlock(required=True),
                                                                ),
                                                                ("slug", wagtail.blocks.CharBlock(required=True)),
                                                                ("answer", wagtail.blocks.RichTextBlock(required=True)),
                                                                (
                                                                    "document",
                                                                    wagtail.documents.blocks.DocumentChooserBlock(
                                                                        required=False
                                                                    ),
                                                                ),
                                                            ],
                                                            required=False,
                                                        )
                                                    ),
                                                ),
                                            ],
                                            required=True,
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    ("paragraph", pages.custom_blocks.APIRichTextBlock()),
                    (
                        "image",
                        wagtail.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock(required=False)),
                                ("alt_text", wagtail.blocks.CharBlock(required=False)),
                                ("link", wagtail.blocks.URLBlock(required=False)),
                                ("alignment", pages.custom_blocks.ImageFormatChoiceBlock(required=False)),
                                (
                                    "identifier",
                                    wagtail.blocks.CharBlock(
                                        help_text="Used by the frontend for Google Analytics.", required=False
                                    ),
                                ),
                            ]
                        ),
                    ),
                    ("html", wagtail.blocks.RawHTMLBlock()),
                ],
                use_json_field=True,
            ),
        ),
    ]
