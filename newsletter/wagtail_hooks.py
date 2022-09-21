from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
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
    list_diplay = (
        "email",
        "name",
        "first_optin_at",
        "double_optin_at",
        "consented_from",
        "consent_withdrawn_at",
        "subscribed",
    )
