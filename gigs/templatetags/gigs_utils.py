from datetime import date

from django import template
from gigs.models import GigPage

register = template.Library()


@register.inclusion_tag("gigs/includes/gigs_listing.html", takes_context=True)
def upcoming_gigs(context, count=3):
    gigs = GigPage.objects.filter(live=True)
    gigs = gigs.filter(date_from__gte=date.today())
    gigs = gigs.all().order_by("date_from")
    return {
        "gigs": gigs[:count],
        # required by the pageurl tag that we want to use within this template
        "request": context["request"],
    }
