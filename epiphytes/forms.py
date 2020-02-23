from django import forms

from .models import EpiphyticOrganism


class EpiphyticOrganismForm(forms.ModelForm):

    class Meta:
        model = EpiphyticOrganism
        fields = ['name']
