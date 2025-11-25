from crowdfunding.models import Campaign, Donation
from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
from django.utils.functional import lazy
from django.utils.translation import gettext_lazy as _
from home.blocks import (
    ButtonBlock,
    FooterCTABlock,
    ImageGridBlock,
    NewsletterSignupBlock,
    ParagraphImageBlock,
)
from home.models import HomePage2
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.tags import ClusterTaggableManager
from streetnoise.models import Page
from taggit.models import Tag, TaggedItemBase
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
from wagtail.api import APIField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.fields import StreamField
from wagtail.images import get_image_model_string
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import FieldPanel
from wagtail.models import Page as WagtailPage
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from .blocks import (
    CrowdfundingRewardsBlock,
    FundersBlock,
    HeadingParagraphBlock,
    LineupBlock,
    NumberBoxesBlock,
    ProgramBlock2,
)

"""
Festival Landing Page


Save the Date (full width) w/ signup CTA

IMAGE Intro Blurb

Musik in der ganzen Stadt IMAGE

IMAGE  Acitivist blurb

Sign up for updates (full width)

---BLOCKS--

choose template

Title cenetered with line below
Paragraph centered
Band Friends
Sponsor logos w/ link
Program
Image Grid

Footer



"""


def get_all_campaigns():
    campaigns = []
    for campaign in Campaign.objects.all():
        campaigns.append((campaign.campaign_name, campaign.campaign_name))
    return campaigns


class FestivalPage2026(Page):
    def __init__(self, *args, **kwargs):
        super(FestivalPage2026, self).__init__(*args, **kwargs)
        self._meta.get_field("crowdfunding_campaign").choices = lazy(get_all_campaigns, list)()

    page_template = models.CharField(
        default="festival2026/homepage.html",
        max_length=255,
        choices=[("festival2026/homepage.html", "Home Page")],
    )

    crowdfunding_body = StreamField(
        [
            ("heading_text", HeadingParagraphBlock()),
            ("paragraph_image", ParagraphImageBlock()),
            ("crowdfunding_rewards", CrowdfundingRewardsBlock()),
            ("footercta", FooterCTABlock()),
            (
                "embed",
                EmbedBlock(
                    icon="media",
                    label=_("Embed media"),
                    help_text=_("Paste a link to a video, audio file, instagram, etc."),
                ),
            ),
        ],
        null=True,
        blank=True,
    )
    body = StreamField(
        [
            ("heading_text", HeadingParagraphBlock()),
            ("paragraph_image", ParagraphImageBlock()),
            ("image_grid", ImageGridBlock()),
            ("number_boxes", NumberBoxesBlock()),
            ("crowdfunding_rewards", CrowdfundingRewardsBlock()),
            ("lineup", LineupBlock()),
            ("funders", FundersBlock(label="Funders & Sponsors")),
            ("program2", ProgramBlock2(label="Program")),
            ("newsletter", NewsletterSignupBlock()),
            (
                "embed",
                EmbedBlock(
                    icon="media",
                    label=_("Embed media"),
                    help_text=_("Paste a link to a video, audio file, instagram, etc."),
                ),
            ),
            ("footercta", FooterCTABlock()),
        ],
        null=True,
        blank=True,
    )

    crowdfunding_campaign = models.CharField(
        default="festival2026/homepage.html",
        max_length=255,
        blank=True,
        choices=[],
    )

    content_panels = Page.content_panels + [
        FieldPanel("page_template", classname="full title"),
        FieldPanel("crowdfunding_campaign", classname="full title"),
        FieldPanel("crowdfunding_body", classname="collapsible collapsed"),
        FieldPanel("body", classname="collapsible collapsed"),
    ]

    def get_template(self, request, *args, **kwargs):
        if self.page_template:
            return self.page_template
        else:
            return "festival2026/homepage.html"

    def get_context(self, request):
        context = super(FestivalPage2026, self).get_context(request)
        homepage = HomePage2.objects.first()
        if self.crowdfunding_campaign:
            campaign = Campaign.objects.get(campaign_name=self.crowdfunding_campaign)
            context["campaign"] = campaign
        context["homepage"] = homepage
        return context
