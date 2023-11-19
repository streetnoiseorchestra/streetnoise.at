from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import GigIndexPage, GigPage


@register(GigIndexPage)
class GigIndexPageTR(TranslationOptions):
    pass


@register(GigPage)
class GigPageTR(TranslationOptions):
    fields = ("body", "body2")
