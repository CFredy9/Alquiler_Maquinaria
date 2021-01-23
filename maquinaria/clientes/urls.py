"""Urls de Clientes"""

#Django 
from django.urls import include, path

#Django rest_framework 
from rest_framework.routers import DefaultRouter

#Views 
from .views import clientes as cliente_views

router = DefaultRouter()
router.register(r'clientes', cliente_views.ClienteViewSet, basename='cliente')

urlpatterns = [
	path('', include(router.urls)),
]