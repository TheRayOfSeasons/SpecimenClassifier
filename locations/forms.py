from django import forms

from .models import Location


class LocationForm(forms.ModelForm):
    """
    A form for adding or updating locations.
    """

    class Meta:
        model = Location
        fields = ['name']
