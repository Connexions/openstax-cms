# Generated by Django 5.0.7 on 2024-07-22 21:25

import pages.custom_blocks
import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0111_alter_rootpage_body_squashed_0130_alter_rootpage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="impact",
            name="making_a_difference",
            field=wagtail.fields.StreamField(
                [
                    (
                        "content",
                        wagtail.blocks.StructBlock(
                            [
                                ("heading", wagtail.blocks.CharBlock()),
                                ("description", wagtail.blocks.RichTextBlock()),
                                (
                                    "stories",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("image", pages.custom_blocks.APIImageChooserBlock(required=False)),
                                                ("story_text", wagtail.blocks.TextBlock(required=False)),
                                                (
                                                    "linked_story",
                                                    wagtail.blocks.PageChooserBlock(
                                                        page_type=["pages.ImpactStory", "news.NewsArticle"]
                                                    ),
                                                ),
                                                ("embedded_video", wagtail.blocks.RawHTMLBlock(required=False)),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                use_json_field=True,
            ),
        ),
    ]
