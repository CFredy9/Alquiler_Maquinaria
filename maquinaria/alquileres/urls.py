"""Urls de Maquinas"""

#Django 
from django.urls import include, path

#Django rest_framework 
from rest_framework.routers import DefaultRouter

#Views 
from .views import alquileres as alquileres_views
from maquinaria.alquileres.views import Estado

router = DefaultRouter()
router.register(r'alquileres', alquileres_views.AlquilerViewSet, basename='alquiler')
#router.register(r'estado', alquileres_views.Update_Estado, basename='estado')

urlpatterns = [
	path('', include(router.urls)),
	path('alquileres/estado/', Estado.as_view(), name='estado'),
]