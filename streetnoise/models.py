from django.db import models
from django.urls import reverse

from wagtail.core.models import Page as WagtailPage
from wagtail.images.edit_handlers import ImageChooserPanel

from home.views import newsletter_subscribe, newsletter_unsubscribe


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

    def get_context(self, request):
        # from home.forms import DonationForm

        context = super(Page, self).get_context(request)
        # donation_page = DonationPage.objects.first()
        # if donation_page is not None:
        #    url = donation_page.get_url()
        #    context["donation_form"] = DonationForm()
        #    context["donation_page_url"] = url
        context["subscribe_page_url"] = reverse(newsletter_subscribe)
        context["unsubscribe_page_url"] = reverse(newsletter_unsubscribe)
        return context

    class Meta:
        abstract = True
