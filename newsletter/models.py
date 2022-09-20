from django.db import models

from birdsong.blocks import DefaultBlocks
from birdsong.models import Campaign, Contact

from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
    FieldPanel,
    MultiFieldPanel,
    FieldRowPanel,
)
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel


class Newsletter(Campaign):
    headline = models.CharField(
        max_length=255, help_text="The headline to use for the newsletter."
    )

    header_background = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        help_text="The image to use for the header backgound.",
        on_delete=models.SET_NULL,
    )

    body = StreamField(DefaultBlocks())

    panels = Campaign.panels + [
        FieldPanel("headline"),
        ImageChooserPanel("header_background"),
        StreamFieldPanel("body"),
    ]


class ExtendedContact(Contact):
    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"

    name = models.CharField(max_length=255)
    first_optin_at = models.DateTimeField(blank=True, null=True)
    double_optin_at = models.DateTimeField(blank=True, null=True)
    consented_from = models.CharField(max_length=255, blank=True, null=True)
    consent_withdrawn_at = models.CharField(max_length=255, blank=True, null=True)
    subscribed = models.BooleanField(
        default=False, help_text="If the user should recieve emails or not"
    )

    panels = [
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("email"),
                        FieldPanel("name"),
                    ]
                ),
            ],
            heading="Contact Info",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("first_optin_at"),
                        FieldPanel("double_optin_at"),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel("consented_from"),
                        FieldPanel("consent_withdrawn_at"),
                    ]
                ),
                FieldPanel("subscribed"),
            ],
            heading="Subscription Status",
        ),
    ]
