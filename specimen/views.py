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
    LocationForm,
    NorthDetailsForm,
    EastDetailsForm,
    WestDetailsForm,
    SouthDetailsForm,
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


class AddDirectionDetailsView(View):
    template_name = 'specimen/direction-details.html'

    def get(self, request, pk, *args, **kwargs):
        context = {}
        context['north_details_form'] = NorthDetailsForm()
        context['east_details_form'] = EastDetailsForm()
        context['west_details_form'] = WestDetailsForm()
        context['south_details_form'] = SouthDetailsForm()
        return render(request, self.template_name, context=context)

    def post(self, request, pk, *args, **kwargs):
        northPH = request.POST.get('northPH')
        eastPH = request.POST.get('eastPH')
        westPH = request.POST.get('westPH')
        southPH = request.POST.get('southPH')
        return reverse_lazy('specimen:detail')



class AddLocationView(CreateView):
    """
    Form view for adding locations.
    """

    template_name = 'specimen/add-location.html'
    model = Location
    form_class = LocationForm

