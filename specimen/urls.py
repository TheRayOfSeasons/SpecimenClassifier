from django.urls import path
from .views import (
    CreateSpecimenView,
    UpdateSpecimenView,
    SpecimenListView,
    SpecimenDetailView,
    AddLocationView,
)


app_name = 'specimen'

urlpatterns = [
    path('', SpecimenListView.as_view(),
        name='list'),
    path('detail/<int:pk>/', SpecimenDetailView.as_view(),
        name='detail'),
    path('new/', CreateSpecimenView.as_view(),
        name='create'),
    path('update/<int:pk>/', UpdateSpecimenView.as_view(),
        name='update'),
    path('add-location/', AddLocationView.as_view(),
        name='new_location'),
]