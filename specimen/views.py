from django.shortcuts import render
from django.views.generic import (
    CreateView
)
from django.views import View
from trees.models import Tree
from .models import (
    Location
)
from .forms import (
    LocationForm
)


class CreateSpecimenView(View):
    template_name = 'specimen/create-specimen.html'
    
    def get(self, request, *args, **kwargs):
        context = {}
        trees = Tree.objects.all()
        localities = Location.objects.all()

        context['trees'] = trees
        context['localities'] = localities

        return render(request, self.template_name, context=context)


class AddLocationView(CreateView):
    template_name = 'specimen/add-location.html'
    model = Location
    form_class = LocationForm

