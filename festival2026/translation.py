from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import FestivalPage2026


@register(FestivalPage2026)
class FestivalPage2026TR(TranslationOptions):
    fields = (
        "crowdfunding_body",
        "body",
    )
