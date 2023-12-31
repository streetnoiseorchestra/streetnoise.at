from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import SongIndexPage, SongPage


@register(SongIndexPage)
class SongIndexPageTR(TranslationOptions):
    fields = ("intro",)


@register(SongPage)
class SongPageTR(TranslationOptions):
    fields = ("description",)
