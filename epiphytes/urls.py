from django.urls import path

from .views import (
    EpiphyticOrganismListView,
    EpiphyticOrganismCreateView,
    EpiphyticOrganismUpdateView,
)


app_name = 'epiphytes'

urlpatterns = [
    path('', EpiphyticOrganismListView.as_view(),
        name='list'),
    path('new/', EpiphyticOrganismCreateView.as_view(),
        name='create'),
    path('update/<int:pk>/', EpiphyticOrganismUpdateView.as_view(),
        name='update')
]