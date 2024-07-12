# Generated by Django 5.0.7 on 2024-07-12 15:07

import pages.custom_blocks
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0096_alter_rootpage_body"),
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
                                (
                                    "image",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("image", wagtail.images.blocks.ImageChooserBlock(required=False)),
                                                ("alt_text", wagtail.blocks.CharBlock(required=False)),
                                                (
                                                    "alignment",
                                                    pages.custom_blocks.ImageFormatChoiceBlock(required=False),
                                                ),
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
                                                                            wagtail.blocks.PageChooserBlock(
                                                                                required=False
                                                                            ),
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
                                                            (
                                                                "link_aria_label",
                                                                wagtail.blocks.CharBlock(required=False),
                                                            ),
                                                        ],
                                                        label="CTA",
                                                        required=False,
                                                    ),
                                                ),
                                            ],
                                            required=False,
                                        ),
                                        collapsed=True,
                                        max_num=1,
                                    ),
                                ),
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
                                        collapsed=True,
                                        max_num=2,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "section",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "cards",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("text", pages.custom_blocks.APIRichTextBlock(required=False)),
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
                                                                            wagtail.blocks.PageChooserBlock(
                                                                                required=False
                                                                            ),
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
                                                            (
                                                                "link_aria_label",
                                                                wagtail.blocks.CharBlock(required=False),
                                                            ),
                                                        ],
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.blocks.StructBlock(
                                                        [
                                                            (
                                                                "image",
                                                                wagtail.images.blocks.ImageChooserBlock(required=False),
                                                            ),
                                                            ("alt_text", wagtail.blocks.CharBlock(required=False)),
                                                            (
                                                                "alignment",
                                                                pages.custom_blocks.ImageFormatChoiceBlock(
                                                                    required=False
                                                                ),
                                                            ),
                                                            (
                                                                "cta",
                                                                wagtail.blocks.StructBlock(
                                                                    [
                                                                        (
                                                                            "text",
                                                                            wagtail.blocks.CharBlock(required=False),
                                                                        ),
                                                                        (
                                                                            "link",
                                                                            wagtail.blocks.StreamBlock(
                                                                                [
                                                                                    (
                                                                                        "external",
                                                                                        wagtail.blocks.URLBlock(
                                                                                            required=False
                                                                                        ),
                                                                                    ),
                                                                                    (
                                                                                        "internal",
                                                                                        wagtail.blocks.PageChooserBlock(
                                                                                            required=False
                                                                                        ),
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
                                                                        (
                                                                            "link_aria_label",
                                                                            wagtail.blocks.CharBlock(required=False),
                                                                        ),
                                                                    ],
                                                                    label="CTA",
                                                                    required=False,
                                                                ),
                                                            ),
                                                        ],
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "style",
                                                    wagtail.blocks.ChoiceBlock(
                                                        choices=[("rounded", "Rounded"), ("square", "Square")]
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                                ("text", pages.custom_blocks.APIRichTextBlock()),
                                ("html", wagtail.blocks.RawHTMLBlock()),
                                (
                                    "image",
                                    wagtail.blocks.StructBlock(
                                        [
                                            ("image", wagtail.images.blocks.ImageChooserBlock(required=False)),
                                            ("alt_text", wagtail.blocks.CharBlock(required=False)),
                                            ("alignment", pages.custom_blocks.ImageFormatChoiceBlock(required=False)),
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
                                                    required=False,
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                                (
                                    "faq",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("question", wagtail.blocks.RichTextBlock(required=True)),
                                                ("slug", wagtail.blocks.CharBlock(required=True)),
                                                ("answer", wagtail.blocks.RichTextBlock(required=True)),
                                                (
                                                    "document",
                                                    wagtail.documents.blocks.DocumentChooserBlock(required=False),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    ("text", pages.custom_blocks.APIRichTextBlock()),
                    ("html", wagtail.blocks.RawHTMLBlock()),
                    (
                        "image",
                        wagtail.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock(required=False)),
                                ("alt_text", wagtail.blocks.CharBlock(required=False)),
                                ("alignment", pages.custom_blocks.ImageFormatChoiceBlock(required=False)),
                                (
                                    "cta",
                                    wagtail.blocks.StructBlock(
                                        [
                                            ("text", wagtail.blocks.CharBlock(required=False)),
                                            (
                                                "link",
                                                wagtail.blocks.StreamBlock(
                                                    [
                                                        ("external", wagtail.blocks.URLBlock(required=False)),
                                                        ("internal", wagtail.blocks.PageChooserBlock(required=False)),
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
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                ],
                use_json_field=True,
            ),
        ),
    ]
