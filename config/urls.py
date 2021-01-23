"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include(('maquinaria.maquinas.urls', 'maquinas'), namespace='maquina')),
    path('', include(('maquinaria.clientes.urls', 'clientes'), namespace='cliente')),
    path('', include(('maquinaria.alquileres.urls', 'alquileres'), namespace='alquiler')),
    path('', include(('maquinaria.usuarios.urls', 'usuarios'), namespace='usuario')),
    path('', include(('maquinaria.reportes.urls', 'reportes'), namespace='reporte')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
