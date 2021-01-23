"""Circles URls"""

#Django
from django.urls import path 

#Views
from maquinaria.reportes.reportes import Reporte


urlpatterns = [
	path('reportes/', Reporte),
]