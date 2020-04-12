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
            'ph_level_1',
            'ph_level_2',
            'ph_level_3',
            'state_of_decay',
            'bark_texture',
            'stain',
        ]
        labels = {
            'state_of_decay': 'State of Decay',
            'bark_texture': 'Bark Texture',
            'stain': 'Stain',
        }
    
    def __init__(self, specimen, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.specimen = specimen


class EastDetailsForm(forms.ModelForm):

    class Meta:
        model = EastDetails
        fields = [
            'ph_level_1',
            'ph_level_2',
            'ph_level_3',
            'state_of_decay',
            'bark_texture',
            'stain',
        ]
        labels = {
            'state_of_decay': 'State of Decay',
            'bark_texture': 'Bark Texture',
            'stain': 'Stain',
        }
    
    def __init__(self, specimen, *args, **kwargs):
        super().__init__(*args, **forms.ModelForm)
        self.specimen = specimen


class WestDetailsForm(forms.ModelForm):

    class Meta:
        model = WestDetails
        fields = [
            'ph_level_1',
            'ph_level_2',
            'ph_level_3',
            'state_of_decay',
            'bark_texture',
            'stain',
        ]
        labels = {
            'state_of_decay': 'State of Decay',
            'bark_texture': 'Bark Texture',
            'stain': 'Stain',
        }
    
    def __init__(self, specimen, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.specimen = specimen


class SouthDetailsForm(forms.ModelForm):

    class Meta:
        model = SouthDetails
        fields = [
            'ph_level_1',
            'ph_level_2',
            'ph_level_3',
            'state_of_decay',
            'bark_texture',
            'stain',
        ]
        labels = {
            'state_of_decay': 'State of Decay',
            'bark_texture': 'Bark Texture',
            'stain': 'Stain',
        }
    
    def __init__(self, specimen, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.specimen = specimen
