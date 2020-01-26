from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView
)
from .models import Tree
from .forms import (
    TreeForm
)
from django.urls import reverse


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

    def get_success_url(self):
        return reverse('trees:list')

