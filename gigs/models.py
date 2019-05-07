from datetime import date

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models
from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class GigIndexPage(Page):
    intro = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    @property
    def events(self):
        events = GigPage.objects.live().descendant_of(self)
        events = events.filter(date_from__gte=date.today())
        events = events.order_by('date_from')

        return events

    def get_context(self, request):
        # Get events
        events = self.events
        # Filter by tag
        tag = request.GET.get('tag')
        if tag:
            events = events.filter(tags__name=tag)

        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(events, 9)  # Show 10 events per page
        try:
            events = paginator.page(page)
        except PageNotAnInteger:
            events = paginator.page(1)
        except EmptyPage:
            events = paginator.page(paginator.num_pages)

        # Update template context
        context = super(GigIndexPage, self).get_context(request)
        context['events'] = events
        return context


GigIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
]

GigIndexPage.promote_panels = [
    MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ImageChooserPanel('feed_image'),
]


class GigPage(Page):
    gigomatic_id = models.CharField(max_length=255, null=True, blank=False)

    date_from = models.DateField("Start date")
    date_to = models.DateField(
        "End date",
        null=True,
        blank=True,
        help_text="Not required if gig is on a single day"
    )
    call_time = models.TimeField("Set time", null=True, blank=True)
    set_time = models.TimeField("Set time", null=True, blank=True)
    end_time = models.TimeField("End time", null=True, blank=True)

    location = models.CharField(max_length=255, null=True, blank=True)
    partner = models.CharField(max_length=255, null=True, blank=True,
                               help_text="The organization we're doing the gig for")
    link = models.URLField(blank=True)
    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The gig banner image",
    )
    content_panels = Page.content_panels + [
        FieldPanel('gigomatic_id', classname="full title"),
        FieldPanel('date_from'),
        FieldPanel('date_to'),
        FieldPanel('call_time'),
        FieldPanel('set_time'),
        FieldPanel('end_time'),
        FieldPanel('location'),
        FieldPanel('partner'),
        FieldPanel('link'),
        FieldPanel('body', classname="full"),
    ]
    promote_panels = Page.promote_panels + [
        ImageChooserPanel('feed_image'),
    ]
