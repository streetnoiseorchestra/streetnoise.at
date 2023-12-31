# Generated by Django 3.0.7 on 2020-06-08 10:47

import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0006_auto_20200608_0800"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("heading", wagtail.blocks.CharBlock(classname="full title")),
                    ("paragraph", wagtail.blocks.RichTextBlock()),
                    ("image", wagtail.images.blocks.ImageChooserBlock(icon="image")),
                    ("embedded_video", wagtail.embeds.blocks.EmbedBlock(classname="full title", icon="media")),
                    (
                        "image_carousel",
                        wagtail.blocks.ListBlock(
                            wagtail.blocks.StructBlock(
                                [
                                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                                    ("caption", wagtail.blocks.TextBlock(required=False)),
                                    ("video", wagtail.embeds.blocks.EmbedBlock(required=False)),
                                ]
                            ),
                            icon="image",
                            template="blog/blocks/carousel.html",
                        ),
                    ),
                    (
                        "button",
                        wagtail.blocks.StructBlock(
                            [
                                ("button_text", wagtail.blocks.CharBlock(blank=True)),
                                ("button_url", wagtail.blocks.URLBlock(label="Button link")),
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="blogpage",
            name="body_de",
            field=wagtail.fields.StreamField(
                [
                    ("heading", wagtail.blocks.CharBlock(classname="full title")),
                    ("paragraph", wagtail.blocks.RichTextBlock()),
                    ("image", wagtail.images.blocks.ImageChooserBlock(icon="image")),
                    ("embedded_video", wagtail.embeds.blocks.EmbedBlock(classname="full title", icon="media")),
                    (
                        "image_carousel",
                        wagtail.blocks.ListBlock(
                            wagtail.blocks.StructBlock(
                                [
                                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                                    ("caption", wagtail.blocks.TextBlock(required=False)),
                                    ("video", wagtail.embeds.blocks.EmbedBlock(required=False)),
                                ]
                            ),
                            icon="image",
                            template="blog/blocks/carousel.html",
                        ),
                    ),
                    (
                        "button",
                        wagtail.blocks.StructBlock(
                            [
                                ("button_text", wagtail.blocks.CharBlock(blank=True)),
                                ("button_url", wagtail.blocks.URLBlock(label="Button link")),
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="blogpage",
            name="body_en",
            field=wagtail.fields.StreamField(
                [
                    ("heading", wagtail.blocks.CharBlock(classname="full title")),
                    ("paragraph", wagtail.blocks.RichTextBlock()),
                    ("image", wagtail.images.blocks.ImageChooserBlock(icon="image")),
                    ("embedded_video", wagtail.embeds.blocks.EmbedBlock(classname="full title", icon="media")),
                    (
                        "image_carousel",
                        wagtail.blocks.ListBlock(
                            wagtail.blocks.StructBlock(
                                [
                                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                                    ("caption", wagtail.blocks.TextBlock(required=False)),
                                    ("video", wagtail.embeds.blocks.EmbedBlock(required=False)),
                                ]
                            ),
                            icon="image",
                            template="blog/blocks/carousel.html",
                        ),
                    ),
                    (
                        "button",
                        wagtail.blocks.StructBlock(
                            [
                                ("button_text", wagtail.blocks.CharBlock(blank=True)),
                                ("button_url", wagtail.blocks.URLBlock(label="Button link")),
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
            ),
        ),
    ]
