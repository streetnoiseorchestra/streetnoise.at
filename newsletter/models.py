from django.db import models

from birdsong.blocks import DefaultBlocks
from birdsong.models import Campaign, Contact

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldPanel,
    MultiFieldPanel,
    FieldRowPanel,
)
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import FieldPanel


class Newsletter(Campaign):
    class Meta:
        verbose_name = "SNOZeitung Issue"
        verbose_name_plural = "SNOZeitung Issues"

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
        FieldPanel("header_background"),
        FieldPanel("body"),
    ]


class NewsletterSubscriber(Contact):
    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"

    name = models.CharField(max_length=255, help_text="The user's name")
    first_optin_at = models.DateTimeField(
        blank=True,
        null=True,
        help_text="When the subscriber first asked to receive newsletters",
    )
    double_optin_at = models.DateTimeField(
        blank=True,
        null=True,
        help_text="When the subscriber confirmed their email address",
    )
    consented_from = models.CharField(
        max_length=255, blank=True, null=True, help_text="Where/How the user consented"
    )
    consent_withdrawn_at = models.CharField(
        max_length=255, blank=True, null=True, help_text="When the user unsubscribed"
    )
    subscribed = models.BooleanField(
        default=False, help_text="If the user should recieve emails or not"
    )
    bounce_score = models.IntegerField(
        default=0, help_text="The subscriber's current bounce score"
    )
    reset_bounce_score_on = models.DateTimeField(
        blank=True, null=True, help_text="When the bounce score should be reset"
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
                FieldPanel("subscribed"),
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
            ],
            heading="Subscription Status",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("bounce_score"),
                        FieldPanel("reset_bounce_score_on"),
                    ]
                ),
            ],
            heading="Bounce Info",
        ),
    ]
