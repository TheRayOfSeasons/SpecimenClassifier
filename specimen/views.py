from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView
)
from django.views import View
from trees.models import Tree
from .models import (
    Specimen,
    Location
)
from .forms import (
    SpecimenForm,
    LocationForm
)


class CreateSpecimenView(CreateView):
    """
    Form view for adding specimens.
    """
    
    model = Specimen
    form_class = SpecimenForm
    template_name = 'specimen/create-specimen.html'

    def get_success_url(self):
        return reverse_lazy('specimen:detail',
            kwargs={'pk': self.object.pk})


class SpecimenListView(ListView):
    """
    Lists all specimens.
    """
    
    model = Specimen
    template_name = 'specimen/list-specimen.html'


class SpecimenDetailView(DetailView):
    """
    Detail view for specimens.
    """

    model = Specimen
    template_name = 'specimen/detail-specimen.html'


class UpdateSpecimenView(UpdateView):
    """
    View for updating specimens.
    """

    model = Specimen
    form_class = SpecimenForm
    template_name = 'specimen/update-specimen.html'

    def get_success_url(self):
        return reverse_lazy('specimen:detail',
            kwargs={'pk': self.object.pk})


class AddLocationView(CreateView):
    """
    Form view for adding locations.
    """

    template_name = 'specimen/add-location.html'
    model = Location
    form_class = LocationForm

