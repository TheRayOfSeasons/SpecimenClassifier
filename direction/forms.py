from django import forms

from .models import (
    NorthDetails,
    EastDetails,
    WestDetails,
    SouthDetails,
)


class NorthDetailsForm(forms.ModelForm):

    class Meta:
        model = NorthDetails
        fields = [
            'ph_level'
        ]

    def __init__(self, specimen, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.specimen = specimen


class EastDetailsForm(forms.ModelForm):

    class Meta:
        model = EastDetails
        fields = [
            'ph_level'
        ]

    def __init__(self, specimen, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.specimen = specimen


class WestDetailsForm(forms.ModelForm):

    class Meta:
        model = WestDetails
        fields = [
            'ph_level'
        ]

    def __init__(self, specimen, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.specimen = specimen


class SouthDetailsForm(forms.ModelForm):

    class Meta:
        model = SouthDetails
        fields = [
            'ph_level'
        ]

    def __init__(self, specimen, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.specimen = specimen
