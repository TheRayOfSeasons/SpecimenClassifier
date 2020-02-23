from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('specimen/', include('specimen.urls')),
    path('trees/', include('trees.urls')),
    path('epiphytes/', include('epiphytes.urls')),
]
