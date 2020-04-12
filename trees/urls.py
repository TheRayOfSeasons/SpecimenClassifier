from django.urls import path
from .views import (
    TreeCreateView,
    TreeListView,
    TreeUpdateView,
)


app_name = 'trees'

urlpatterns = [
    path('list/', TreeListView.as_view(),
        name='list'),
    path('create/', TreeCreateView.as_view(),
        name='create'),
    path('<int:pk>/update/', TreeCreateView.as_view(),
        name='update'),
]
