from django.db import models
from django.urls import reverse
from home.views import newsletter_subscribe, newsletter_unsubscribe
from wagtail.images.edit_handlers import FieldPanel
from wagtail.models import Page as WagtailPage


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
        FieldPanel("feed_image"),
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
