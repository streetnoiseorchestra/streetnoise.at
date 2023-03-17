from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django import forms
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
from wagtail.snippets.models import register_snippet
from taggit.models import Tag
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    FieldRowPanel,
    StreamFieldPanel,
)
from wagtail.api import APIField
from wagtail.core.models import Page as WagtailPage
from wagtail.images import get_image_model_string
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

from home.models import HomePage2
from home.blocks import (
    ButtonBlock,
    ImageGridBlock,
    ParagraphImageBlock,
    NewsletterSignupBlock,
)
from streetnoise.models import Page

from .blocks import (
    NumberBoxesBlock,
    LineupBlock,
    FundersBlock,
    HeadingParagraphBlock,
    ProgramBlock,
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


class FestivalPage2023(Page):
    page_template = models.CharField(
        default="festival2023/homepage.html",
        max_length=255,
        choices=[("festival2023/homepage.html", "Home Page")],
    )
    body = StreamField(
        [
            ("heading_text", HeadingParagraphBlock()),
            ("paragraph_image", ParagraphImageBlock()),
            ("image_grid", ImageGridBlock()),
            ("number_boxes", NumberBoxesBlock()),
            ("lineup", LineupBlock()),
            ("funders", FundersBlock()),
            ("program", ProgramBlock()),
            ("newsletter", NewsletterSignupBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("page_template", classname="full title"),
        StreamFieldPanel("body"),
    ]

    def get_template(self, requeist, *args, **kwargs):
        if self.page_template:
            return self.page_template
        else:
            return "festival2023/homepage.html"

    def get_context(self, request):
        context = super(FestivalPage2023, self).get_context(request)
        homepage = HomePage2.objects.first()
        context["homepage"] = homepage
        return context
