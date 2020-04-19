from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from dashboard.views import DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('admin/', admin.site.urls),
    path('specimen/', include('specimen.urls')),
    path('trees/', include('trees.urls')),
    path('epiphytes/', include('epiphytes.urls')),
    path('locations/', include('locations.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
