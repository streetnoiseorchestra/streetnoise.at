from wagtail import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class ImageCarouselBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.TextBlock(required=False)
    video = EmbedBlock(required=False)

    class Meta:
        template = "blog/blocks/carousel.html"
        # icon = 'image'
