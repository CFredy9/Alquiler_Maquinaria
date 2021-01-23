"""Urls de Maquinas"""

#Django 
from django.urls import include, path

#Django rest_framework 
from rest_framework.routers import DefaultRouter

#Views 
from .views import maquinas as maquina_views

router = DefaultRouter()
router.register(r'maquinas', maquina_views.MaquinaViewSet, basename='maquinas')

urlpatterns = [
	path('', include(router.urls)),
]