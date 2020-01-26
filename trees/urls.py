from django.urls import path
from .views import (
    TreeListView,
    TreeCreateView
)


app_name = 'trees'

urlpatterns = [
    path('list/', TreeListView.as_view(),
        name='list'),
    path('new/', TreeCreateView.as_view(),
        name='create')
]