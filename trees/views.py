from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)
from .models import Tree
from .forms import (
    TreeForm
)
from django.urls import reverse_lazy


class TreeListView(ListView):
    template_name = 'trees/list-tree.html'
    model = Tree


class TreeCreateView(CreateView):
    '''
    View for adding new trees in the database
    '''

    template_name = 'trees/create-tree.html'
    model = Tree
    form_class = TreeForm
    success_url = reverse_lazy('trees:list')


class TreeUpdateView(UpdateView):
    '''
    View for adding new trees in the database
    '''

    template_name = 'trees/update-tree.html'
    model = Tree
    form_class = TreeForm
    success_url = reverse_lazy('trees:list')
