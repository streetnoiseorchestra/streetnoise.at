from datetime import date, datetime
from django.utils.translation import gettext_lazy as _

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, FieldRowPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.images.edit_handlers import FieldPanel
from wagtail.fields import StreamField


from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from home.blocks import ButtonBlock


class GigIndexPage(Page):
    intro = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    @property
    def events(self):
        events = GigPage.objects.live().descendant_of(self)
        events = events.filter(date_from__gte=date.today())
        events = events.order_by("date_from")

        return events

    def get_context(self, request):
        # Get events
        events = self.events
        # Filter by tag
        tag = request.GET.get("tag")
        if tag:
            events = events.filter(tags__name=tag)

        # Pagination
        page = request.GET.get("page")
        paginator = Paginator(events, 9)  # Show 10 events per page
        try:
            events = paginator.page(page)
        except PageNotAnInteger:
            events = paginator.page(1)
        except EmptyPage:
            events = paginator.page(paginator.num_pages)

        # Update template context
        context = super(GigIndexPage, self).get_context(request)
        context["events"] = events
        return context


GigIndexPage.content_panels = [
    FieldPanel("title", classname="full title"),
    FieldPanel("intro", classname="full"),
]

GigIndexPage.promote_panels = [
    MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    FieldPanel("feed_image"),
]


class GigPage(Page):
    gigomatic_id = models.CharField(max_length=255, null=True, blank=True)

    date_from = models.DateField(_("Start date"))
    date_to = models.DateField(
        _("End date"),
        null=True,
        blank=True,
        help_text=_("Not required if gig is on a single day"),
    )
    call_time = models.TimeField(_("Call time"), null=True, blank=True)
    set_time = models.TimeField(_("Set time"), null=True, blank=True)
    end_time = models.TimeField(_("End time"), null=True, blank=True)

    location = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Where is the gig taking place?"),
    )
    partner = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Which organization are we doing the gig with?"),
    )
    link = models.URLField(
        blank=True,
        help_text=_("A link to a blog, facebook page, or other site about this gig."),
    )
    body = RichTextField(
        _("Details"), blank=True, help_text=_("A sentence or two describing the gig.")
    )

    body2 = StreamField(
        [
            ("heading", blocks.CharBlock(classname="full title")),
            (
                "paragraph",
                blocks.RichTextBlock(
                    features=[
                        "h1",
                        "h2",
                        "h3",
                        "h4",
                        "h5",
                        "bold",
                        "italic",
                        "strikethrough",
                        "ol",
                        "ul",
                        "hr",
                        "link",
                        "document-link",
                        "image",
                        "embed",
                        "blockquote",
                    ]
                ),
            ),
            ("image", ImageChooserBlock(icon="image")),
            (
                "embedded_video",
                EmbedBlock(
                    icon="media",
                    label=_("Embed media"),
                    help_text=_("Paste a link to a video, audio file, instagram, etc."),
                ),
            ),
            ("button", ButtonBlock()),
        ],
        null=True,
        blank=True,
        help_text=_("A sentence or two describing the gig."),
    )
    feed_image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name=_("Gig Image"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "A photo representing the gig or organization. Best if it has a 2x1 aspect ratio (example: 800x400)."
        ),
    )
    content_panels = Page.content_panels + [
        FieldPanel(
            "feed_image",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("date_from"),
                        FieldPanel("date_to"),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel("call_time"),
                        FieldPanel("set_time"),
                        FieldPanel("end_time"),
                    ]
                ),
            ],
            _("Date & Time"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("location"),
                FieldPanel("partner"),
                FieldPanel("link"),
                FieldPanel("body2", classname="full"),
                FieldPanel("gigomatic_id", classname=""),
            ],
            _("Gig Details"),
        ),
    ]
    promote_panels = Page.promote_panels + []

    @property
    def date_start_time(self):
        if self.call_time is None:
            return self.date_from
        return datetime.combine(self.date_from, self.call_time)

    @property
    def date_end_time(self):
        if self.end_time is None:
            if self.date_to is None:
                return self.date_from
            return self.date_to
        if self.date_to is None:
            return datetime.combine(self.date_from, self.end_time)
        else:
            return datetime.combine(self.date_to, self.end_time)

    def get_context(self, request, *args, **kwargs):
        from blog.models import BlogIndexPage
        from home.models import HomePage2

        context = super().get_context(request, *args, **kwargs)
        context["blog_index_page"] = BlogIndexPage.objects.first()
        context["homepage"] = HomePage2.objects.first()
        return context
