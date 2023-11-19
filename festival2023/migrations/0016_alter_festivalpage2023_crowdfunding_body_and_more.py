# Generated by Django 4.1.9 on 2023-06-30 07:51

import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("festival2023", "0015_alter_festivalpage2023_body_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="festivalpage2023",
            name="crowdfunding_body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "heading_text",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(max_length=255, required=True),
                                ),
                                (
                                    "text",
                                    wagtail.blocks.RichTextBlock(
                                        features=[
                                            "h1",
                                            "h2",
                                            "h3",
                                            "h4",
                                            "h5",
                                            "bold",
                                            "italic",
                                            "strikethrough",
                                            "ol",
                                            "ul",
                                            "hr",
                                            "link",
                                            "document-link",
                                            "image",
                                            "embed",
                                            "blockquote",
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "paragraph_image",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(max_length=255, required=True),
                                ),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(group="Image", required=True),
                                ),
                                (
                                    "image_alignment",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("", "Select Image alignment"),
                                            ("left", "Image Left"),
                                            ("right", "Image Right"),
                                        ],
                                        group="Image",
                                    ),
                                ),
                                (
                                    "aspect_ratio",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("", "Select Aspect Ratio of Images"),
                                            ("1:1", "1:1 Square"),
                                            ("1:1 sm", "1:1 Square (smaller)"),
                                            ("3:2", "3:2"),
                                            ("4:3", "4:3 (traditional)"),
                                            ("16:9", "16:9 (widescreen)"),
                                        ]
                                    ),
                                ),
                                (
                                    "with_shadow",
                                    wagtail.blocks.BooleanBlock(
                                        default=True,
                                        group="Image",
                                        help_text="Add a shadow to the image, good for photographs",
                                        required=False,
                                    ),
                                ),
                                (
                                    "background_color",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("", "Section Background Color"),
                                            ("green", "SNO Green"),
                                            ("orange", "SNO Orange"),
                                            ("blue", "Blue"),
                                            ("white", "White"),
                                        ]
                                    ),
                                ),
                                (
                                    "body",
                                    wagtail.blocks.RichTextBlock(
                                        features=[
                                            "bold",
                                            "italic",
                                            "strikethrough",
                                            "ol",
                                            "ul",
                                            "hr",
                                            "link",
                                            "document-link",
                                            "blockquote",
                                        ],
                                        required=True,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "crowdfunding_rewards",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(max_length=255, required=True),
                                ),
                                (
                                    "description2",
                                    wagtail.blocks.RichTextBlock(
                                        features=[
                                            "bold",
                                            "italic",
                                            "strikethrough",
                                            "ol",
                                            "ul",
                                            "hr",
                                            "link",
                                            "document-link",
                                            "image",
                                            "blockquote",
                                        ]
                                    ),
                                ),
                                (
                                    "rewards",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "title",
                                                    wagtail.blocks.CharBlock(max_length=255, required=True),
                                                ),
                                                (
                                                    "description",
                                                    wagtail.blocks.TextBlock(max_length=255, required=True),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(required=False),
                                                ),
                                                (
                                                    "price",
                                                    wagtail.blocks.CharBlock(max_length=255, required=True),
                                                ),
                                                (
                                                    "payment_link",
                                                    wagtail.blocks.URLBlock(required=True),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "footercta",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "cta_title",
                                    wagtail.blocks.CharBlock(blank=True, verbose_name="CTA Title"),
                                ),
                                (
                                    "cta_subtitle",
                                    wagtail.blocks.CharBlock(blank=True, verbose_name="CTA Subtitle"),
                                ),
                                (
                                    "cta_button1",
                                    wagtail.blocks.CharBlock(blank=True, verbose_name="Button 1 Text"),
                                ),
                                (
                                    "cta_button2",
                                    wagtail.blocks.CharBlock(blank=True, verbose_name="Button 2 Text"),
                                ),
                                (
                                    "cta_button1_url",
                                    wagtail.blocks.URLBlock(form_classname="full title"),
                                ),
                                (
                                    "cta_button2_url",
                                    wagtail.blocks.URLBlock(form_classname="full title"),
                                ),
                            ]
                        ),
                    ),
                    (
                        "embed",
                        wagtail.embeds.blocks.EmbedBlock(
                            help_text="Paste a link to a video, audio file, instagram, etc.",
                            icon="media",
                            label="Embed media",
                        ),
                    ),
                ],
                blank=True,
                null=True,
                use_json_field=None,
            ),
        ),
        migrations.AlterField(
            model_name="festivalpage2023",
            name="crowdfunding_body_de",
            field=wagtail.fields.StreamField(
                [
                    (
                        "heading_text",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(max_length=255, required=True),
                                ),
                                (
                                    "text",
                                    wagtail.blocks.RichTextBlock(
                                        features=[
                                            "h1",
                                            "h2",
                                            "h3",
                                            "h4",
                                            "h5",
                                            "bold",
                                            "italic",
                                            "strikethrough",
                                            "ol",
                                            "ul",
                                            "hr",
                                            "link",
                                            "document-link",
                                            "image",
                                            "embed",
                                            "blockquote",
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "paragraph_image",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(max_length=255, required=True),
                                ),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(group="Image", required=True),
                                ),
                                (
                                    "image_alignment",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("", "Select Image alignment"),
                                            ("left", "Image Left"),
                                            ("right", "Image Right"),
                                        ],
                                        group="Image",
                                    ),
                                ),
                                (
                                    "aspect_ratio",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("", "Select Aspect Ratio of Images"),
                                            ("1:1", "1:1 Square"),
                                            ("1:1 sm", "1:1 Square (smaller)"),
                                            ("3:2", "3:2"),
                                            ("4:3", "4:3 (traditional)"),
                                            ("16:9", "16:9 (widescreen)"),
                                        ]
                                    ),
                                ),
                                (
                                    "with_shadow",
                                    wagtail.blocks.BooleanBlock(
                                        default=True,
                                        group="Image",
                                        help_text="Add a shadow to the image, good for photographs",
                                        required=False,
                                    ),
                                ),
                                (
                                    "background_color",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("", "Section Background Color"),
                                            ("green", "SNO Green"),
                                            ("orange", "SNO Orange"),
                                            ("blue", "Blue"),
                                            ("white", "White"),
                                        ]
                                    ),
                                ),
                                (
                                    "body",
                                    wagtail.blocks.RichTextBlock(
                                        features=[
                                            "bold",
                                            "italic",
                                            "strikethrough",
                                            "ol",
                                            "ul",
                                            "hr",
                                            "link",
                                            "document-link",
                                            "blockquote",
                                        ],
                                        required=True,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "crowdfunding_rewards",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(max_length=255, required=True),
                                ),
                                (
                                    "description2",
                                    wagtail.blocks.RichTextBlock(
                                        features=[
                                            "bold",
                                            "italic",
                                            "strikethrough",
                                            "ol",
                                            "ul",
                                            "hr",
                                            "link",
                                            "document-link",
                                            "image",
                                            "blockquote",
                                        ]
                                    ),
                                ),
                                (
                                    "rewards",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "title",
                                                    wagtail.blocks.CharBlock(max_length=255, required=True),
                                                ),
                                                (
                                                    "description",
                                                    wagtail.blocks.TextBlock(max_length=255, required=True),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(required=False),
                                                ),
                                                (
                                                    "price",
                                                    wagtail.blocks.CharBlock(max_length=255, required=True),
                                                ),
                                                (
                                                    "payment_link",
                                                    wagtail.blocks.URLBlock(required=True),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "footercta",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "cta_title",
                                    wagtail.blocks.CharBlock(blank=True, verbose_name="CTA Title"),
                                ),
                                (
                                    "cta_subtitle",
                                    wagtail.blocks.CharBlock(blank=True, verbose_name="CTA Subtitle"),
                                ),
                                (
                                    "cta_button1",
                                    wagtail.blocks.CharBlock(blank=True, verbose_name="Button 1 Text"),
                                ),
                                (
                                    "cta_button2",
                                    wagtail.blocks.CharBlock(blank=True, verbose_name="Button 2 Text"),
                                ),
                                (
                                    "cta_button1_url",
                                    wagtail.blocks.URLBlock(form_classname="full title"),
                                ),
                                (
                                    "cta_button2_url",
                                    wagtail.blocks.URLBlock(form_classname="full title"),
                                ),
                            ]
                        ),
                    ),
                    (
                        "embed",
                        wagtail.embeds.blocks.EmbedBlock(
                            help_text="Paste a link to a video, audio file, instagram, etc.",
                            icon="media",
                            label="Embed media",
                        ),
                    ),
                ],
                blank=True,
                null=True,
                use_json_field=None,
            ),
        ),
        migrations.AlterField(
            model_name="festivalpage2023",
            name="crowdfunding_body_en",
            field=wagtail.fields.StreamField(
                [
                    (
                        "heading_text",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(max_length=255, required=True),
                                ),
                                (
                                    "text",
                                    wagtail.blocks.RichTextBlock(
                                        features=[
                                            "h1",
                                            "h2",
                                            "h3",
                                            "h4",
                                            "h5",
                                            "bold",
                                            "italic",
                                            "strikethrough",
                                            "ol",
                                            "ul",
                                            "hr",
                                            "link",
                                            "document-link",
                                            "image",
                                            "embed",
                                            "blockquote",
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "paragraph_image",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(max_length=255, required=True),
                                ),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(group="Image", required=True),
                                ),
                                (
                                    "image_alignment",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("", "Select Image alignment"),
                                            ("left", "Image Left"),
                                            ("right", "Image Right"),
                                        ],
                                        group="Image",
                                    ),
                                ),
                                (
                                    "aspect_ratio",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("", "Select Aspect Ratio of Images"),
                                            ("1:1", "1:1 Square"),
                                            ("1:1 sm", "1:1 Square (smaller)"),
                                            ("3:2", "3:2"),
                                            ("4:3", "4:3 (traditional)"),
                                            ("16:9", "16:9 (widescreen)"),
                                        ]
                                    ),
                                ),
                                (
                                    "with_shadow",
                                    wagtail.blocks.BooleanBlock(
                                        default=True,
                                        group="Image",
                                        help_text="Add a shadow to the image, good for photographs",
                                        required=False,
                                    ),
                                ),
                                (
                                    "background_color",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("", "Section Background Color"),
                                            ("green", "SNO Green"),
                                            ("orange", "SNO Orange"),
                                            ("blue", "Blue"),
                                            ("white", "White"),
                                        ]
                                    ),
                                ),
                                (
                                    "body",
                                    wagtail.blocks.RichTextBlock(
                                        features=[
                                            "bold",
                                            "italic",
                                            "strikethrough",
                                            "ol",
                                            "ul",
                                            "hr",
                                            "link",
                                            "document-link",
                                            "blockquote",
                                        ],
                                        required=True,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "crowdfunding_rewards",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(max_length=255, required=True),
                                ),
                                (
                                    "description2",
                                    wagtail.blocks.RichTextBlock(
                                        features=[
                                            "bold",
                                            "italic",
                                            "strikethrough",
                                            "ol",
                                            "ul",
                                            "hr",
                                            "link",
                                            "document-link",
                                            "image",
                                            "blockquote",
                                        ]
                                    ),
                                ),
                                (
                                    "rewards",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "title",
                                                    wagtail.blocks.CharBlock(max_length=255, required=True),
                                                ),
                                                (
                                                    "description",
                                                    wagtail.blocks.TextBlock(max_length=255, required=True),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(required=False),
                                                ),
                                                (
                                                    "price",
                                                    wagtail.blocks.CharBlock(max_length=255, required=True),
                                                ),
                                                (
                                                    "payment_link",
                                                    wagtail.blocks.URLBlock(required=True),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "footercta",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "cta_title",
                                    wagtail.blocks.CharBlock(blank=True, verbose_name="CTA Title"),
                                ),
                                (
                                    "cta_subtitle",
                                    wagtail.blocks.CharBlock(blank=True, verbose_name="CTA Subtitle"),
                                ),
                                (
                                    "cta_button1",
                                    wagtail.blocks.CharBlock(blank=True, verbose_name="Button 1 Text"),
                                ),
                                (
                                    "cta_button2",
                                    wagtail.blocks.CharBlock(blank=True, verbose_name="Button 2 Text"),
                                ),
                                (
                                    "cta_button1_url",
                                    wagtail.blocks.URLBlock(form_classname="full title"),
                                ),
                                (
                                    "cta_button2_url",
                                    wagtail.blocks.URLBlock(form_classname="full title"),
                                ),
                            ]
                        ),
                    ),
                    (
                        "embed",
                        wagtail.embeds.blocks.EmbedBlock(
                            help_text="Paste a link to a video, audio file, instagram, etc.",
                            icon="media",
                            label="Embed media",
                        ),
                    ),
                ],
                blank=True,
                null=True,
                use_json_field=None,
            ),
        ),
    ]
