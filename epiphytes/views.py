from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView
)

from .forms import EpiphyticOrganismForm
from .models import EpiphyticOrganism


class EpiphyticOrganismListView(ListView):
    model = EpiphyticOrganism
    template_name = 'epiphytes/epiphyte-list.html'


class EpiphyticOrganismCreateView(CreateView):
    model = EpiphyticOrganism
    form_class = EpiphyticOrganismForm
    template_name = 'epiphytes/epiphyte-create.html'
    success_url = reverse_lazy('epiphytes:list')


class EpiphyticOrganismUpdateView(UpdateView):
    model = EpiphyticOrganism
    form_class = EpiphyticOrganismForm
    template_name = 'epiphytes/epiphyte-update.html'
    success_url = reverse_lazy('epiphytes:list')
