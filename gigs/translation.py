from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import GigPage, GigIndexPage

@register(GigIndexPage)
class GigIndexPageTR(TranslationOptions):
    pass
    # fields = (
    # )
@register(GigPage)
class GigPageTR(TranslationOptions):
    fields = (
    )
