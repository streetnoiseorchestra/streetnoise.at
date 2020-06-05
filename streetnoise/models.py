from django.db import models
from wagtail.core.models import Page as WagtailPage
from wagtail.images.edit_handlers import ImageChooserPanel


class Page(WagtailPage):
    feed_image = models.ForeignKey(
        "wagtailimages.Image",
        help_text="The image shown on Facebook and other social media",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    promote_panels = WagtailPage.promote_panels + [
        ImageChooserPanel("feed_image"),
    ]

    class Meta:
        abstract = True
