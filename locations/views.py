from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.shortcuts import render

from .forms import LocationForm
from .models import Location


class LocationListView(ListView):
    """
    View for listing locations.
    """

    model = Location
    template_name = 'locations/list_location.html'


class LocationAddView(CreateView):
    """
    Form view for adding locations.
    """

    model = Location
    form_class = LocationForm
    template_name = 'locations/add_location.html'


class LocationUpdateView(UpdateView):
    """
    Form view for updating locations.
    """

    model = Location
    form_class = LocationForm
    template_name = 'locations/update_location.html'
