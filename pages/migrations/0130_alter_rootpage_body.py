# Generated by Django 5.0.7 on 2024-07-22 18:25

import pages.custom_blocks
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0129_alter_rootpage_body"),
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
                                (
                                    "content",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "cards_block",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "cards",
                                                            wagtail.blocks.ListBlock(
                                                                wagtail.blocks.StructBlock(
                                                                    [
                                                                        (
                                                                            "text",
                                                                            pages.custom_blocks.APIRichTextBlock(),
                                                                        ),
                                                                        (
                                                                            "cta_block",
                                                                            wagtail.blocks.ListBlock(
                                                                                wagtail.blocks.StructBlock(
                                                                                    [
                                                                                        (
                                                                                            "text",
                                                                                            wagtail.blocks.CharBlock(
                                                                                                required=True
                                                                                            ),
                                                                                        ),
                                                                                        (
                                                                                            "aria_label",
                                                                                            wagtail.blocks.CharBlock(
                                                                                                required=False
                                                                                            ),
                                                                                        ),
                                                                                        (
                                                                                            "target",
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
                                                                                                required=True,
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    label="Link",
                                                                                    required=False,
                                                                                ),
                                                                                default=[],
                                                                                label="Call To Action",
                                                                                max_num=1,
                                                                            ),
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ),
                                                        (
                                                            "config",
                                                            wagtail.blocks.StreamBlock(
                                                                [
                                                                    (
                                                                        "card_size",
                                                                        wagtail.blocks.IntegerBlock(
                                                                            help_text="Width multiplier. default 27.",
                                                                            min_value=0,
                                                                        ),
                                                                    ),
                                                                    (
                                                                        "card_style",
                                                                        wagtail.blocks.ChoiceBlock(
                                                                            choices=[
                                                                                ("rounded", "Rounded"),
                                                                                ("square", "Square"),
                                                                            ]
                                                                        ),
                                                                    ),
                                                                ],
                                                                block_counts={
                                                                    "card_size": {"max_num": 1},
                                                                    "card_style": {"max_num": 1},
                                                                },
                                                                required=False,
                                                            ),
                                                        ),
                                                    ],
                                                    label="Cards Block",
                                                ),
                                            ),
                                            ("text", pages.custom_blocks.APIRichTextBlock()),
                                            ("html", wagtail.blocks.RawHTMLBlock()),
                                            (
                                                "cta_block",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "actions",
                                                            wagtail.blocks.ListBlock(
                                                                wagtail.blocks.StructBlock(
                                                                    [
                                                                        (
                                                                            "text",
                                                                            wagtail.blocks.CharBlock(required=True),
                                                                        ),
                                                                        (
                                                                            "aria_label",
                                                                            wagtail.blocks.CharBlock(required=False),
                                                                        ),
                                                                        (
                                                                            "target",
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
                                                                                required=True,
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    label="Button",
                                                                    required=False,
                                                                ),
                                                                default=[],
                                                                label="Actions",
                                                                max_num=2,
                                                            ),
                                                        )
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                                ("image", pages.custom_blocks.APIImageChooserBlock(required=False)),
                                ("image_alt", wagtail.blocks.CharBlock(required=False)),
                                (
                                    "config",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "image_alignment",
                                                wagtail.blocks.ChoiceBlock(
                                                    choices=[
                                                        ("left", "Left"),
                                                        ("right", "Right"),
                                                        ("topLeft", "Top Left"),
                                                        ("topRight", "Top Right"),
                                                        ("bottomLeft", "Bottom Left"),
                                                        ("bottomRight", "Bottom Right"),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "image_size",
                                                wagtail.blocks.ChoiceBlock(
                                                    choices=[
                                                        ("auto", "Auto"),
                                                        ("contain", "Contain"),
                                                        ("cover", "Cover"),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "padding",
                                                wagtail.blocks.IntegerBlock(
                                                    help_text="Padding multiplier. default 0.", min_value=0
                                                ),
                                            ),
                                            (
                                                "background_color",
                                                wagtail.blocks.RegexBlock(
                                                    error_mssages={"invalid": "not a valid hex color."},
                                                    help_text="eg: #ff0000",
                                                    regex="#[a-zA-Z0-9]{6}",
                                                ),
                                            ),
                                        ],
                                        block_counts={
                                            "background_color": {"max_num": 1},
                                            "image_alignment": {"max_num": 1},
                                            "image_size": {"max_num": 1},
                                            "padding": {"max_num": 1},
                                        },
                                        required=False,
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
                                    "content",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "cards_block",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "cards",
                                                            wagtail.blocks.ListBlock(
                                                                wagtail.blocks.StructBlock(
                                                                    [
                                                                        (
                                                                            "text",
                                                                            pages.custom_blocks.APIRichTextBlock(),
                                                                        ),
                                                                        (
                                                                            "cta_block",
                                                                            wagtail.blocks.ListBlock(
                                                                                wagtail.blocks.StructBlock(
                                                                                    [
                                                                                        (
                                                                                            "text",
                                                                                            wagtail.blocks.CharBlock(
                                                                                                required=True
                                                                                            ),
                                                                                        ),
                                                                                        (
                                                                                            "aria_label",
                                                                                            wagtail.blocks.CharBlock(
                                                                                                required=False
                                                                                            ),
                                                                                        ),
                                                                                        (
                                                                                            "target",
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
                                                                                                required=True,
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    label="Link",
                                                                                    required=False,
                                                                                ),
                                                                                default=[],
                                                                                label="Call To Action",
                                                                                max_num=1,
                                                                            ),
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ),
                                                        (
                                                            "config",
                                                            wagtail.blocks.StreamBlock(
                                                                [
                                                                    (
                                                                        "card_size",
                                                                        wagtail.blocks.IntegerBlock(
                                                                            help_text="Width multiplier. default 27.",
                                                                            min_value=0,
                                                                        ),
                                                                    ),
                                                                    (
                                                                        "card_style",
                                                                        wagtail.blocks.ChoiceBlock(
                                                                            choices=[
                                                                                ("rounded", "Rounded"),
                                                                                ("square", "Square"),
                                                                            ]
                                                                        ),
                                                                    ),
                                                                ],
                                                                block_counts={
                                                                    "card_size": {"max_num": 1},
                                                                    "card_style": {"max_num": 1},
                                                                },
                                                                required=False,
                                                            ),
                                                        ),
                                                    ],
                                                    label="Cards Block",
                                                ),
                                            ),
                                            ("text", pages.custom_blocks.APIRichTextBlock()),
                                            ("html", wagtail.blocks.RawHTMLBlock()),
                                            (
                                                "cta_block",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "actions",
                                                            wagtail.blocks.ListBlock(
                                                                wagtail.blocks.StructBlock(
                                                                    [
                                                                        (
                                                                            "text",
                                                                            wagtail.blocks.CharBlock(required=True),
                                                                        ),
                                                                        (
                                                                            "aria_label",
                                                                            wagtail.blocks.CharBlock(required=False),
                                                                        ),
                                                                        (
                                                                            "target",
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
                                                                                required=True,
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    label="Button",
                                                                    required=False,
                                                                ),
                                                                default=[],
                                                                label="Actions",
                                                                max_num=2,
                                                            ),
                                                        )
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                                (
                                    "config",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "background_color",
                                                wagtail.blocks.RegexBlock(
                                                    error_mssages={"invalid": "not a valid hex color."},
                                                    help_text="eg: #ff0000",
                                                    regex="#[a-zA-Z0-9]{6}",
                                                ),
                                            ),
                                            (
                                                "padding",
                                                wagtail.blocks.IntegerBlock(
                                                    help_text="Padding multiplier. default 0.", min_value=0
                                                ),
                                            ),
                                            (
                                                "text_alignment",
                                                wagtail.blocks.ChoiceBlock(
                                                    choices=[("center", "Center"), ("left", "Left"), ("right", "Right")]
                                                ),
                                            ),
                                        ],
                                        block_counts={
                                            "background_color": {"max_num": 1},
                                            "padding": {"max_num": 1},
                                            "text_alignment": {"max_num": 1},
                                        },
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "divider",
                        wagtail.blocks.StructBlock(
                            [
                                ("image", pages.custom_blocks.APIImageChooserBlock()),
                                (
                                    "config",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "alignment",
                                                wagtail.blocks.ChoiceBlock(
                                                    choices=[
                                                        ("center", "Center"),
                                                        ("content_left", "Left side of content."),
                                                        ("content_right", "Right side of content."),
                                                        ("body_left", "Left side of window."),
                                                        ("body_right", "Right side of window."),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "width",
                                                wagtail.blocks.RegexBlock(
                                                    error_messages={
                                                        "invalid": "must be valid css measurement. eg: 30px, 50%, 10rem"
                                                    },
                                                    regex="^[0-9]+(px|%|rem)$",
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "height",
                                                wagtail.blocks.RegexBlock(
                                                    error_messages={
                                                        "invalid": "must be valid css measurement. eg: 30px, 50%, 10rem"
                                                    },
                                                    regex="^[0-9]+(px|%|rem)$",
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "offset_vertical",
                                                wagtail.blocks.RegexBlock(
                                                    error_messages={
                                                        "invalid": "must be valid css measurement. eg: 30px, 50%, 10rem"
                                                    },
                                                    regex="^\\-?[0-9]+(px|%|rem)$",
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "offset_horizontal",
                                                wagtail.blocks.RegexBlock(
                                                    error_messages={
                                                        "invalid": "must be valid css measurement. eg: 30px, 50%, 10rem"
                                                    },
                                                    regex="^\\-?[0-9]+(px|%|rem)$",
                                                    required=False,
                                                ),
                                            ),
                                        ],
                                        block_counts={
                                            "alignment": {"max_num": 1},
                                            "height": {"max_num": 1},
                                            "offset_horizontal": {"max_num": 1},
                                            "offset_vertical": {"max_num": 1},
                                            "width": {"max_num": 1},
                                        },
                                        required=False,
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
