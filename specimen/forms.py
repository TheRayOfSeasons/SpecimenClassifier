from django import forms

from locations.models import Location
from trees.models import Tree

from .models import Specimen


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
        )
        labels = {
            'dbh': 'DBH',
            'collection_date': 'Collection Date',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['host_tree'].queryset = (
            Tree.objects.all())
        self.fields['location'].queryset = (
            Location.objects.all())
