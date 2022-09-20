from django.conf import settings
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

from .utils import unique_slugify
from .blocks import ImageCarouselBlock

from streetnoise.models import Page

from home.blocks import ButtonBlock

import datetime


class BlogIndexPageAbstract(Page):
    header_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Header image"),
    )

    class Meta:
        verbose_name = _("Blog index")
        abstract = True


class BlogCategoryAbstract(models.Model):
    name = models.CharField(max_length=80, unique=True, verbose_name=_("Category Name"))
    slug = models.SlugField(unique=True, max_length=80)
    parent = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="children",
        help_text=_(
            "Categories, unlike tags, can have a hierarchy. You might have a "
            "Jazz category, and under that have children categories for Bebop"
            " and Big Band. Totally optional."
        ),
        on_delete=models.CASCADE,
    )
    description = models.CharField(max_length=500, blank=True)

    class Meta:
        abstract = True
        ordering = ["name"]
        verbose_name = _("Blog Category")
        verbose_name_plural = _("Blog Categories")

    panels = [
        FieldPanel("name"),
        FieldPanel("parent"),
        FieldPanel("description"),
    ]

    def __str__(self):
        return self.name

    def clean(self):
        if self.parent:
            parent = self.parent
            if self.parent == self:
                raise ValidationError("Parent category cannot be self.")
            if parent.parent and parent.parent == self:
                raise ValidationError("Cannot have circular Parents.")

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, self.name)
        return super().save(*args, **kwargs)


class BlogCategoryBlogPageAbstract(models.Model):
    category = models.ForeignKey(
        "BlogCategory",
        related_name="+",
        verbose_name=_("Category"),
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True

    page = ParentalKey("BlogPage", related_name="categories")
    panels = [
        FieldPanel("category"),
    ]


class BlogPageTagAbstract(TaggedItemBase):
    content_object = ParentalKey("BlogPage", related_name="tagged_items")

    class Meta:
        abstract = True


def limit_author_choices():
    """Limit choices in blog author field based on config settings"""
    LIMIT_AUTHOR_CHOICES = getattr(settings, "BLOG_LIMIT_AUTHOR_CHOICES_GROUP", None)
    if LIMIT_AUTHOR_CHOICES:
        if isinstance(LIMIT_AUTHOR_CHOICES, str):
            limit = Q(groups__name=LIMIT_AUTHOR_CHOICES)
        else:
            limit = Q()
            for s in LIMIT_AUTHOR_CHOICES:
                limit = limit | Q(groups__name=s)
        if getattr(settings, "BLOG_LIMIT_AUTHOR_CHOICES_ADMIN", False):
            limit = limit | Q(is_staff=True)
    else:
        limit = {"is_staff": True}
    return limit


class BlogPageAbstract(Page):
    body = StreamField(
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
            (
                "image_carousel",
                blocks.ListBlock(
                    ImageCarouselBlock(),
                    template="blog/blocks/carousel.html",
                    icon="image",
                ),
            ),
            ("button", ButtonBlock()),
        ],
        null=True,
        blank=True,
    )
    intro = models.CharField(
        max_length=512,
        blank=True,
        null=True,
        verbose_name=_("Post summary"),
        help_text=_("A short summary of the post in one or two sentences."),
    )
    tags = ClusterTaggableManager(through="BlogPageTag", blank=True)
    date = models.DateField(
        _("Post date"),
        default=datetime.datetime.today,
        help_text=_(
            "This date may be displayed on the blog post. It is not "
            "used to schedule posts to go live at a later date."
        ),
    )
    header_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Header image"),
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        limit_choices_to=limit_author_choices,
        verbose_name=_("Author"),
        on_delete=models.SET_NULL,
        related_name="author_pages",
    )

    search_fields = Page.search_fields + [
        index.SearchField("body"),
    ]
    blog_categories = ParentalManyToManyField(
        "BlogCategory", through="BlogCategoryBlogPage", blank=True
    )

    hide_author = models.BooleanField(
        default=False, help_text="Hide the author sign-off."
    )
    hide_header_title = models.BooleanField(
        default=False,
        help_text="Hide the blog title from the header image on the blog post page.",
    )
    hide_header_overlay = models.BooleanField(
        default=False,
        help_text="Do not apply the subtle color overlay to the header image on the blog post page.",
    )
    extra_css = models.TextField(blank=True, verbose_name="Extra CSS")

    settings_panels = [
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("go_live_at"),
                        FieldPanel("expire_at"),
                    ],
                    classname="label-above",
                ),
            ],
            "Scheduled publishing",
            classname="publishing",
        ),
        FieldPanel("date"),
        FieldPanel("author"),
        MultiFieldPanel(
            [
                FieldPanel("hide_author"),
                FieldPanel("hide_header_title"),
                FieldPanel("hide_header_overlay"),
                FieldPanel("extra_css"),
            ],
            "Appearance",
            classname="appearance",
        ),
    ]

    def save_revision(self, *args, **kwargs):
        if not self.author:
            self.author = self.owner
        return super().save_revision(*args, **kwargs)

    def get_absolute_url(self):
        return self.url

    class Meta:
        abstract = True
        verbose_name = _("Blog page")
        verbose_name_plural = _("Blog pages")

    api_fields = [APIField("body")]
    content_panels = [
        FieldPanel("title", classname="full title"),
        FieldPanel("intro", classname="full"),
        MultiFieldPanel(
            [
                FieldPanel("tags"),
                FieldPanel("blog_categories"),
            ],
            heading="Tags and Categories",
        ),
        ImageChooserPanel("header_image"),
        StreamFieldPanel("body"),
    ]
