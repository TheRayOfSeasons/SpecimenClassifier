from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import (
    CreateView
)
from django.views import View
from trees.models import Tree
from .models import (
    Specimen,
    Location
)
from .forms import (
    LocationForm
)


class CreateSpecimenView(CreateView):
    template_name = 'specimen/create-specimen.html'
    
    def get_context_data(self, **kwargs):
        context = super(CreateSpecimenView, self).get_context_data(**kwargs)
        trees = Tree.objects.all()
        localities = Location.objects.all()
        context['trees'] = trees
        context['localities'] = localities
        return context

    def get_success_url(self, request, *args, **kwargs):
        return reverse('specimen:create')
        

class AddLocationView(CreateView):
    template_name = 'specimen/add-location.html'
    model = Location
    form_class = LocationForm

