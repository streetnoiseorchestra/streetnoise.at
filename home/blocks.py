from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class FestivalBandsBlock(blocks.StructBlock):
    name = blocks.CharBlock(classname="full title")
    location = blocks.CharBlock(classname="full title")
    logo = ImageChooserBlock()
    link1_text = blocks.CharBlock(classname="full title")
    link1_url = blocks.URLBlock(classname="full title")
    link2_text = blocks.CharBlock(classname="full title")
    link2_url = blocks.URLBlock(classname="full title")

    class Meta:
        template = "home/blocks/festival_bands.html"


class TimelineHeaderBlock(blocks.StructBlock):
    title = blocks.CharBlock()

    class Meta:
        template = "home/blocks/timeline_header.html"


class TimelineItemBlock(blocks.StructBlock):
    icon = blocks.CharBlock()
    title = blocks.CharBlock(label="Time")
    detail = blocks.CharBlock(label="Name")
    small_detail = blocks.CharBlock(required=False, label="Extra Detail")

    class Meta:
        template = "home/blocks/timeline_item.html"


class MerchItemBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    title = blocks.CharBlock()
    price = blocks.CharBlock()
    detail = blocks.CharBlock()

    class Meta:
        template = "home/blocks/merch_item.html"


class InfoItemBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    detail = blocks.RichTextBlock()

    class Meta:
        template = "home/blocks/info_item.html"


class ImageTileBlock(blocks.StreamBlock):
    image = ImageChooserBlock()

    class Meta:
        template = "home/blocks/image_tile.html"


class FooterCTABlock(blocks.StructBlock):
    cta_title = blocks.CharBlock(blank=True, verbose_name="CTA Title")
    cta_subtitle = blocks.CharBlock(blank=True, verbose_name="CTA Subtitle")
    cta_button1 = blocks.CharBlock(blank=True, verbose_name="Button 1 Text")
    cta_button2 = blocks.CharBlock(blank=True, verbose_name="Button 2 Text")
    cta_button1_url = blocks.URLBlock(classname="full title")
    cta_button2_url = blocks.URLBlock(classname="full title")

    class Meta:
        icon = "placeholder"
        label = "Footer CTA"
        admin_text = "The Call-To-Action at the bottom above the footer"
        template = "home/blocks/footer_cta.html"
