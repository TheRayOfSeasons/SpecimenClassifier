from django.urls import path

from .views import (
    CreateSpecimenView,
    UpdateSpecimenView,
    SpecimenListView,
    SpecimenDetailView,
    AddLocationView,
    AddDirectionDetailsView,
    SpecimenSamplesFormView,
    NorthDeleteSampleImageView,
    EastDeleteSampleImageView,
    WestDeleteSampleImageView,
    SouthDeleteSampleImageView
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
    path('new-direction-details/<int:pk>/', AddDirectionDetailsView.as_view(),
        name='new_direction_details'),
    path('direction-samples/<int:pk>/', SpecimenSamplesFormView.as_view(),
        name='samples'),
    path('north/delete/<int:pk>/', NorthDeleteSampleImageView.as_view(),
        name='delete_north'),
    path('east/delete/<int:pk>/', EastDeleteSampleImageView.as_view(),
        name='delete_east'),
    path('west/delete/<int:pk>/', WestDeleteSampleImageView.as_view(),
        name='delete_west'),
    path('south/delete/<int:pk>/', SouthDeleteSampleImageView.as_view(),
        name='delete_south'),
]