from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import FestivalPage2023


@register(FestivalPage2023)
class FestivalPage2023TR(TranslationOptions):
    fields = (
        "crowdfunding_body",
        "body",
    )
