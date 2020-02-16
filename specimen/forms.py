from django import forms
from django.forms import (
    BaseFormSet,
    formset_factory
)
from .models import (
    Location,
    Specimen,
    NorthDetails,
    EastDetails,
    WestDetails,
    SouthDetails
)
from trees.models import Tree


class LocationForm(forms.ModelForm):
    """
    A form for creating locations. 
    """

    class Meta:
        model = Location
        fields = ['name']


class SpecimenForm(forms.ModelForm):
    """
    A form for creating and updating specimens.
    """

    class Meta:
        model = Specimen
        fields = (
            'name',
            'code',
            'host_tree',
            'location',
            'latitude',
            'longhitude',
            'dbh',
            'collection_date',
            'state_of_decay',
            'bark_texture',
            'stain',
        )
        labels = {
            'dbh': 'DBH',
            'collection_date': 'Collection Date',
            'state_of_decay': 'State of Decay',
            'bark_texture': 'Bark Texture',
            'stain': 'Stain',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['host_tree'].queryset = (
            Tree.objects.all())
        self.fields['location'].queryset = (
            Location.objects.all())


class NorthDetailsForm(forms.ModelForm):
    class Meta:
        model = NorthDetails
        fields = (
            'ph_level',
        )
        labels = {
            'ph_level': 'PH Level'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EastDetailsForm(forms.ModelForm):
    class Meta:
        model = EastDetails
        fields = (
            'ph_level',
        )
        labels = {
            'ph_level': 'PH Level'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class WestDetailsForm(forms.ModelForm):
    class Meta:
        model = WestDetails
        fields = (
            'ph_level',
        )
        labels = {
            'ph_level': 'PH Level'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SouthDetailsForm(forms.ModelForm):
    class Meta:
        model = SouthDetails
        fields = (
            'ph_level',
        )
        labels = {
            'ph_level': 'PH Level'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)