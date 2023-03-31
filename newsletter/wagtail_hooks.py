from django.utils.html import escape
from django.core.exceptions import ObjectDoesNotExist
from django.utils.http import urlencode

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.core import hooks
from wagtail.rich_text import LinkHandler
from wagtail.rich_text.pages import PageLinkHandler
from wagtail.documents.rich_text import DocumentLinkHandler
from wagtail.core.models import Site

from birdsong.options import CampaignAdmin

from .models import Newsletter, NewsletterSubscriber
from .filters import ContactFilter


@modeladmin_register
class NewsletterAdmin(CampaignAdmin):
    campaign = Newsletter
    menu_label = "SNOZeitung"
    menu_icon = "mail"
    menu_order = 200
    contact_class = NewsletterSubscriber
    contact_filter_class = ContactFilter


@modeladmin_register
class SubscriberAdmin(ModelAdmin):
    menu_order = 201
    model = NewsletterSubscriber
    menu_label = "SNOZ. Subscribers"
    menu_icon = "user"
    list_display = (
        "email",
        "name",
        "subscribed",
    )


class AbsoluteLink(object):
    @classmethod
    def getAbsoluteLink(cls, page, qps):
        try:
            root_path = Site.get_site_root_paths()
            # that is probably not ideal but worked for me
            root_url = root_path[0].root_url
            page_url = page.url
            full_url = f"{root_url}{page_url}"
            params = urlencode(qps)
            return f'<a href="{escape(full_url)}?{params}">'
        except (ObjectDoesNotExist, KeyError):
            return "<a>"


class PageAbsoluteLinkHandler(PageLinkHandler):
    identifier = "page"

    @classmethod
    def expand_db_attributes(cls, attrs):
        try:
            page = cls.get_instance(attrs)
            return AbsoluteLink.getAbsoluteLink(page)
        except (ObjectDoesNotExist, KeyError):
            return "<a>"


class DocumentAbsoluteLinkHandler(DocumentLinkHandler):
    identifier = "document"

    @classmethod
    def expand_db_attributes(cls, attrs):
        try:
            document = cls.get_instance(attrs)
            return AbsoluteLink.getAbsoluteLink(document)
        except (ObjectDoesNotExist, KeyError):
            return "<a>"


def make_page_utm_handler(context):
    class PageUtmLinkHandler(PageLinkHandler):
        identifier = "page"

        @classmethod
        def expand_db_attributes(cls, attrs):
            try:
                page = cls.get_instance(attrs)
                params = {
                    "utm_source": "SNOZeitung",
                    "utm_medium": "email",
                    "utm_campaign": context["self"].name,
                }
                return AbsoluteLink.getAbsoluteLink(page, params)
            except (ObjectDoesNotExist, KeyError):
                return "<a>"

    return PageUtmLinkHandler


def make_document_utm_handler(context):
    class DocumentUtmLinkHandler(DocumentLinkHandler):
        identifier = "document"

        @classmethod
        def expand_db_attributes(cls, attrs):
            try:
                document = cls.get_instance(attrs)
                params = {
                    "utm_source": "SNOZeitung",
                    "utm_medium": "email",
                    "utm_campaign": context["self"].name,
                }
                return AbsoluteLink.getAbsoluteLink(document, params)
            except (ObjectDoesNotExist, KeyError):
                return "<a>"

    return DocumentUtmLinkHandler


# uncommenting this enables absolute rewrites for the entire website
# @hooks.register("register_rich_text_features")
def register_link_handler(context):
    def hook(features):
        # features.register_link_type(PageAbsoluteLinkHandler)
        # features.register_link_type(DocumentAbsoluteLinkHandler)
        features.register_link_type(make_page_utm_handler(context))
        features.register_link_type(make_document_utm_handler(context))

    return hook


from birdsong.views import editor
from django import shortcuts
from django.template import loader
from wagtail import hooks
from wagtail import rich_text


def birdsong_render(
    request, template_name, context, content_type=None, status=None, using=None
):
    with hooks.register_temporarily(
        "register_rich_text_features", register_link_handler(context)
    ):
        rich_text.features.has_scanned_for_features = False
        return shortcuts.render(
            request,
            template_name,
            context,
            content_type=content_type,
            status=status,
            using=using,
        )


def birdsong_render_to_string(template, context):
    with hooks.register_temporarily(
        "register_rich_text_features", register_link_handler
    ):
        rich_text.features.has_scanned_for_features = False
        return loader.render_to_string(template, context)


editor.render = birdsong_render
editor.render_to_string = birdsong_render_to_string
