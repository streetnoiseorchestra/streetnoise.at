from django_filters import FilterSet
from django_filters.filters import AllValuesFilter

from .models import NewsletterSubscriber


class ContactFilter(FilterSet):
    location = AllValuesFilter()

    class Meta:
        model = NewsletterSubscriber
        fields = ("subscribed",)
