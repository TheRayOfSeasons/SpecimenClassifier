from django.urls import path

from .views import LocationAddView
from .views import LocationListView
from .views import LocationUpdateView


app_name = 'locations'

urlpatterns = [
    path('', LocationListView.as_view(), name='list'),

    path(
        'create/',
        LocationAddView.as_view(),
        name='create'),

    path(
        'update/<int:pk>/',
        LocationUpdateView.as_view(),
        name='update'),
]
