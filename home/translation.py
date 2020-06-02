from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import HomePage2, FestivalPage, GigRequestPage, GigType, ImpressumPage, DataPrivacyPage, DonationPage, GenericPage


@register(HomePage2)
class HomePage2TR(TranslationOptions):
    fields = (
            'menu_festival',
            'menu_who_we_are',
            'menu_upcoming_gigs',
            'menu_merch',
            'menu_join_us',
            'menu_request_gig',
            'menu_contact',
            'about_text',
            'whoweare_title',
            'whoweare_text',
            'gigs_title',
            'gigs_subtitle',
            'merch_title',
            'merch_subtitle',
            'merch_text',
            'merch_items',
            'donate_title',
            'donate_online',
            'donate_offline',
            'donate_footer',
            'join_us_title',
            'join_us_subtitle',
            'join_us_text',
            'join_us_infos',
            'cta_title',
            'cta_subtitle',
            'cta_button1',
            'cta_button2',
    )

@register(FestivalPage)
class FestivalPageTR(TranslationOptions):
    fields = (
            'menu_festival',
            'menu_who_we_are',
            'menu_upcoming_gigs',
            'menu_merch',
            'menu_join_us',
            'menu_request_gig',
            'menu_contact',
            'festival_intro_title',
            'festival_intro_title2',
            'festival_intro_text',
            'festival_intro_text2',
            'festival_intro_footer',
            'festival_program_title',
            'festival_program_content',
            'festival_program_timeline',
            'about_text',
            'whoweare_title',
            'whoweare_text',
            'gigs_title',
            'gigs_subtitle',
            'merch_title',
            'merch_subtitle',
            'merch_text',
            'merch_items',
            'donate_title',
            'donate_online',
            'donate_offline',
            'donate_footer',
            'join_us_title',
            'join_us_subtitle',
            'join_us_text',
            'join_us_infos',
            'cta_title',
            'cta_subtitle',
            'cta_button1',
            'cta_button2',
    )


@register(GigType)
class GigTypeTR(TranslationOptions):
    fields = (
        'name',
    )


@register(GigRequestPage)
class GigRequestPageTR(TranslationOptions):
    fields = ()

@register(GenericPage)
class GenericPageTR(TranslationOptions):
        fields = ['content']

@register(ImpressumPage)
class ImpressumPageTR(TranslationOptions):
        fields = ['impressum_content']


@register(DataPrivacyPage)
class DataPrivacyPageTR(TranslationOptions):
        fields = ['privacy_content']


@register(DonationPage)
class DonationPageTR(TranslationOptions):
        fields = [
                'donation_intro',
                'label_donation_amount',
                'label_donation',
                'label_donation_detail',
                'thank_you',
                'thank_you_text',
        ]
