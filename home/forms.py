from django import forms

from .models import GigRequest, GigType


class GigRequestForm(forms.Form):
    '''
    A form for requesting a gig
    https://docs.djangoproject.com/en/2.2/ref/forms
    '''

    widget = forms.TextInput(attrs={'class': 'input is-large'})
    widget_date = forms.TextInput(attrs={'class': 'input is-large', 'type': 'date'})
    contact_name = forms.CharField(max_length=100, widget=widget)
    contact_email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'input is-large', 'type': 'email'}))
    contact_org = forms.CharField(max_length=100, widget=widget)
    event_date = forms.DateField(widget=widget_date)
    event_time = forms.TimeField(
        widget=forms.TextInput(attrs={'class': 'input is-large', 'type': 'time'}))
    deadline_date = forms.DateField(widget=widget_date)
    event_type = forms.ModelChoiceField(queryset=GigType.objects.all(),
                                        widget=forms.Select(attrs={'class': 'is-large'}))
    event_occasion = forms.CharField(max_length=100, widget=widget)
    location = forms.CharField(max_length=255, widget=widget)
    donation_amount = forms.IntegerField(widget=widget, required=False)
    details = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea is-large'}))

    class Meta:
        model = GigRequest
        fields = [
            'contact_name',
            'contact_email',
            'contact_org',
            'event_date',
            'event_time',
            'deadline_date',
            'event_type',
            'event_occasion',
            'location',
            'donation_amount',
            'details',
        ]
