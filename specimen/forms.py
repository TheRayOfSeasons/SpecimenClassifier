from django import forms
from django.forms import (
    BaseFormSet,
    formset_factory
)
from .models import (
    Location,
    Specimen
)
from trees.models import Tree


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ['name']


class SpecimenForm(forms.ModelForm):

    class Meta:
        model = Specimen
        fields = ['name', 'code', 'host_tree', '']
        

# class SpecimenForm(forms.ModelForm):



class SpecimenBaseFormSet(BaseFormSet):

    def clean(self):
        return


# SpecimenFormSet = formset_factory()