from django.db import models
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class NumberBoxesBlock(blocks.StructBlock):
    boxes = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("value", blocks.CharBlock(required=True, max_length=40)),
                ("label", blocks.TextBlock(required=True, max_length=200)),
            ]
        )
    )

    class Meta:
        template = "festival2023/blocks/number_boxes_block.html"
        icon = "grip"
        label = "Number Boxes"


class LineupBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=255)
    performers = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("name", blocks.CharBlock(required=True, max_length=255)),
                ("location", blocks.CharBlock(required=True, max_length=255)),
                ("website", blocks.URLBlock(required=False)),
                ("social", blocks.URLBlock(required=False)),
                ("logo", ImageChooserBlock(required=True)),
            ]
        )
    )

    class Meta:
        template = "festival2023/blocks/lineup_block.html"
        label = "Lineup"


class SponsorBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=True, max_length=255)
    logo = ImageChooserBlock(required=False)
    url = blocks.URLBlock(required=False)


class FundersBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=255)
    funders = blocks.ListBlock(SponsorBlock())

    class Meta:
        template = "festival2023/blocks/funders_block.html"
        label = "Funders"


class HeadingParagraphBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=255)
    text = blocks.RichTextBlock(
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
    )

    class Meta:
        template = "festival2023/blocks/heading_paragraph_block.html"
        label = "Heading + Paragraph"


class TimelineHeaderBlock(blocks.StructBlock):
    title = blocks.CharBlock()

    class Meta:
        template = "festival2023/blocks/timeline_header.html"


class TimelineItemBlock(blocks.StructBlock):
    icon = blocks.CharBlock()
    title = blocks.CharBlock(label="Time")
    detail = blocks.CharBlock(label="Name")
    small_detail = blocks.CharBlock(required=False, label="Extra Detail")

    class Meta:
        template = "festival2023/blocks/timeline_item.html"


class ProgramBlock(blocks.StructBlock):
    heading = models.CharField(max_length=100, blank=True)
    timeline = StreamField(
        [
            ("heading", TimelineHeaderBlock(label="Timeline Heading")),
            ("item", TimelineItemBlock(label="Timeline Item")),
        ],
        null=True,
        blank=True,
    )
    descriptions = StreamField(
        [
            ("heading", blocks.CharBlock(classname="full title")),
            ("paragraph", blocks.RichTextBlock()),
        ],
        null=True,
        blank=True,
    )
