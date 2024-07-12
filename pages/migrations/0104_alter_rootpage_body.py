# Generated by Django 5.0.7 on 2024-07-12 18:59

import pages.custom_blocks
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0103_alter_rootpage_body"),
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
                                ("text", pages.custom_blocks.APIRichTextBlock()),
                                ("image", pages.custom_blocks.APIImageChooserBlock(required=False)),
                                (
                                    "cta",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("text", wagtail.blocks.CharBlock(required=False)),
                                                (
                                                    "link",
                                                    wagtail.blocks.StreamBlock(
                                                        [
                                                            ("external", wagtail.blocks.URLBlock(required=False)),
                                                            (
                                                                "internal",
                                                                wagtail.blocks.PageChooserBlock(required=False),
                                                            ),
                                                            (
                                                                "document",
                                                                wagtail.documents.blocks.DocumentChooserBlock(
                                                                    required=False
                                                                ),
                                                            ),
                                                        ],
                                                        required=False,
                                                    ),
                                                ),
                                                ("link_aria_label", wagtail.blocks.CharBlock(required=False)),
                                            ],
                                            required=False,
                                        ),
                                        label="CTA",
                                        max_num=2,
                                    ),
                                ),
                                (
                                    "config",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "alignment",
                                                wagtail.blocks.ChoiceBlock(
                                                    choices=[
                                                        ("left", "Left"),
                                                        ("right", "Right"),
                                                        ("topLeft", "Top Left"),
                                                        ("topRight", "Top Right"),
                                                        ("bottomLeft", "Bottom Left"),
                                                        ("bottomRight", "Bottom Right"),
                                                    ],
                                                    max_num=1,
                                                ),
                                            ),
                                            (
                                                "size",
                                                wagtail.blocks.ChoiceBlock(
                                                    choices=[
                                                        ("auto", "Left"),
                                                        ("curtain", "Right"),
                                                        ("cover", "Cover"),
                                                    ],
                                                    max_num=1,
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "section",
                        wagtail.blocks.StreamBlock(
                            [
                                (
                                    "cards",
                                    wagtail.blocks.StructBlock(
                                        [
                                            ("text", pages.custom_blocks.APIRichTextBlock()),
                                            (
                                                "cta",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        ("text", wagtail.blocks.CharBlock(required=False)),
                                                        (
                                                            "link",
                                                            wagtail.blocks.StreamBlock(
                                                                [
                                                                    (
                                                                        "external",
                                                                        wagtail.blocks.URLBlock(required=False),
                                                                    ),
                                                                    (
                                                                        "internal",
                                                                        wagtail.blocks.PageChooserBlock(required=False),
                                                                    ),
                                                                    (
                                                                        "document",
                                                                        wagtail.documents.blocks.DocumentChooserBlock(
                                                                            required=False
                                                                        ),
                                                                    ),
                                                                ],
                                                                required=False,
                                                            ),
                                                        ),
                                                        ("link_aria_label", wagtail.blocks.CharBlock(required=False)),
                                                    ],
                                                    label="CTA",
                                                ),
                                            ),
                                            (
                                                "config",
                                                wagtail.blocks.StreamBlock(
                                                    [
                                                        (
                                                            "corner_style",
                                                            wagtail.blocks.ChoiceBlock(
                                                                choices=[("rounded", "Rounded"), ("square", "Square")]
                                                            ),
                                                        )
                                                    ],
                                                    max_num=1,
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                                ("text", pages.custom_blocks.APIRichTextBlock()),
                                ("html", wagtail.blocks.RawHTMLBlock()),
                            ],
                            icon="form",
                        ),
                    ),
                    ("text", pages.custom_blocks.APIRichTextBlock()),
                    ("html", wagtail.blocks.RawHTMLBlock()),
                ],
                use_json_field=True,
            ),
        ),
    ]
