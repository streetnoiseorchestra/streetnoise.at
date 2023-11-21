import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.images.edit_handlers import FieldPanel
from wagtail.models import Page
from wagtailmarkdown.fields import MarkdownField


class SongIndexPage(Page):
    intro = RichTextField(blank=True)

    @property
    def songs(self):
        songs = SongPage.objects.descendant_of(self).live()
        songs = sorted(songs, key=lambda x: (x.status, x.title))
        return songs

    def get_context(self, request):
        from home.models import HomePage2

        context = super(SongIndexPage, self).get_context(request)
        context["homepage"] = HomePage2.objects.first()
        print(context)
        return context


SongIndexPage.content_panels = [
    FieldPanel("title", classname="full title"),
    FieldPanel("intro", classname="full"),
]


class SongPage(Page):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        RETIRED = "retired", "Retired"

    snorga_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    arrangement_credits = models.CharField(max_length=255, null=True, blank=True)
    composition_credits = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, choices=Status.choices, default=Status.ACTIVE)
    description = MarkdownField(_("Description"), blank=True, help_text=_("A sentence or two describing the song."))
    arrangement_notes = MarkdownField(
        _("Arrangement Notes"), blank=True, help_text=_("Our notes for the arrangement"), null=True
    )
    lyrics = MarkdownField(_("Lyrics"), blank=True, null=True)
    last_played_date = models.DateField(_("Last Played"), blank=True, null=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("status"),
                FieldPanel("last_played_date"),
                FieldPanel("arrangement_credits"),
                FieldPanel("composition_credits"),
                FieldPanel("description", classname="full"),
                FieldPanel("arrangement_notes", classname="full"),
                FieldPanel("lyrics", classname="full"),
            ],
            _("Song Details"),
        ),
    ]
    promote_panels = Page.promote_panels + []

    def get_context(self, request, *args, **kwargs):
        from home.models import HomePage2

        context = super().get_context(request, *args, **kwargs)
        context["song_index_page"] = SongIndexPage.objects.first()
        context["homepage"] = HomePage2.objects.first()
        print(context)
        return context

    @property
    def parent(self):
        return self.get_parent()
