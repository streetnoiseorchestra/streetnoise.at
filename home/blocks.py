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


class ImageTileBlock(blocks.StreamBlock):
    image = ImageChooserBlock()

    class Meta:
        template = "home/blocks/image_tile.html"
        icon = "image"
        label = "Image Tile (old)"


class ImageTileBlock2Value(blocks.StructValue):
    def image_class(self):
        aspect_ratio = self.get("aspect_ratio")
        if aspect_ratio == "1:1":
            return "is-1by1"
        if aspect_ratio == "1:1 sm":
            return "is-128x128 p-1"
        elif aspect_ratio == "3:2":
            return "is-3by2"
        elif aspect_ratio == "4:3":
            return "is-4by3"
        elif aspect_ratio == "16:9":
            return "is-16by9"
        return ""


class ImageTileBlock2(blocks.StructBlock):
    class Meta:
        admin_text = "Warning: All images should have the same aspect ratio"
        template = "home/blocks/image_tile2.html"
        icon = "image"
        label = "Image Tile (new)"
        value_class = ImageTileBlock2Value

    aspect_ratio = blocks.ChoiceBlock(
        required=True,
        default="3:2",
        choices=[
            ("", "Select Aspect Ratio of Images"),
            ("1:1", "1:1 Square"),
            ("1:1 sm", "1:1 Square (smaller)"),
            ("3:2", "3:2"),
            ("4:3", "4:3 (traditional)"),
            ("16:9", "16:9 (widescreen)"),
        ],
    )

    images = blocks.ListBlock(
        AttributableImageBlock(),
        icon="image",
    )


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


class ParagraphImageBlock2Value(blocks.StructValue):
    def bg_class(self):
        bg_class = self.get("background_color")
        if bg_class == "green":
            return "is-primary"
        if bg_class == "orange":
            return "is-orange"
        elif bg_class == "blue":
            return "is-info"
        elif bg_class == "white":
            return "is-white"
        return ""

    def image_class(self):
        with_shadow = self.get("with_shadow")
        if with_shadow:
            return "image-prettify"
        return ""


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

    with_shadow = blocks.BooleanBlock(
        help_text="Add a shadow to the image, good for photographs",
        group="Image",
        required=False,
        default=True,
    )

    background_color = blocks.ChoiceBlock(
        required=True,
        default="green",
        choices=[
            ("", "Section Background Color"),
            ("green", "SNO Green"),
            ("orange", "SNO Orange"),
            ("blue", "Blue"),
            ("white", "White"),
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
        value_class = ParagraphImageBlock2Value
