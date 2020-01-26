from django.urls import path
from .views import (
    CreateSpecimenView,
    AddLocationView
)


app_name = 'specimen'

urlpatterns = [
    path('new/', CreateSpecimenView.as_view(),
        name='create'),
    path('add-location/', AddLocationView.as_view(),
        name='new_location'),
]