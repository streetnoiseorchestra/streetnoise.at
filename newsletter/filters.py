from django import forms
from django_filters import FilterSet
from django_filters.filters import BooleanFilter

from .models import NewsletterSubscriber

CHOICES = ((True, "Confirmed SNOZeitung Subscribers"),)


class ContactFilter(FilterSet):
    subscribed = BooleanFilter(
        field_name="subscribed",
        label="Recipients",
        widget=forms.RadioSelect(attrs={"class": "form-control"}, choices=CHOICES),
    )

    class Meta:
        model = NewsletterSubscriber
        fields = ("subscribed",)
