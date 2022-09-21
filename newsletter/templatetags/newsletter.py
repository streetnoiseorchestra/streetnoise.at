from django import template
from django.utils.http import urlencode
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag()
def email_utm(campaign):
    r = urlencode(
        {
            "utm_source": "SNOZeitung",
            "utm_medium": "email",
            "utm_campaign": campaign.name,
        }
    )
    return mark_safe(r)
