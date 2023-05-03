from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock


class ImageCarouselBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.TextBlock(required=False)
    video = EmbedBlock(required=False)

    class Meta:
        template = "blog/blocks/carousel.html"
        # icon = 'image'
