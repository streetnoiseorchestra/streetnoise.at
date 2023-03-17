from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock


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


class NewsletterSignupBlock(blocks.StructBlock):
    cta_title = blocks.CharBlock(blank=True, verbose_name="Title")
    cta_subtitle = blocks.CharBlock(blank=True, verbose_name="Subtitle")
    newsletter_type = blocks.ChoiceBlock(
        required=True,
        default="generic",
        choices=[
            ("", "Select Type of Newsletter"),
            ("generic-newsletter", "Generic"),
            ("festival-newsletter", "Festival (Green)"),
        ],
    )

    class Meta:
        icon = "placeholder"
        label = "Newsletter Signup"
        admin_text = "The Newsletter signup form at the bottom above the footer"
        template = "home/blocks/newsletter_signup.html"


class ButtonBlock(blocks.StructBlock):
    button_text = blocks.CharBlock(blank=True)
    button_url = blocks.URLBlock(label="Button link")

    class Meta:
        icon = "placeholder"
        label = "Button"
        admin_text = "Add a big button for someone to push"
        template = "home/blocks/button.html"


class AttributableImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    caption = blocks.TextBlock(required=False)
    attribution = blocks.TextBlock(required=False, verbose_name="Photographer Credit")
    attribution_url = blocks.URLBlock(required=False, vervose_name="Photographer URL")

    class Meta:
        icon = "image"
        label = "Image with Attribution"


class ImageGridBlock(blocks.StructBlock):
    images = blocks.ListBlock(
        AttributableImageBlock(),
        template="home/blocks/image_grid.html",
        icon="image",
    )

    class Meta:
        admin_text = "Warning: Works best with images with 4x3 ratio."
        template = "home/blocks/image_grid.html"
        icon = "image"
        label = "Image Grid"


class ParagraphImageBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=255)
    image = ImageChooserBlock(required=True, group="Image")

    image_alignment = blocks.ChoiceBlock(
        required=True,
        default="left",
        group="Image",
        choices=[
            ("", "Select Image alignment"),
            ("left", "Image Left"),
            ("right", "Image Right"),
        ],
    )
    body = blocks.RichTextBlock(
        required=True,
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
    )

    class Meta:
        template = "home/blocks/paragraph_image_block.html"
        label = "Paragraph + Image"
