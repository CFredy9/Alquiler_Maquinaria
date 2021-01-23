"""Modelo clientes"""

#Django
from django.db import models

#Utilities
from maquinaria.utils.models import CRideModel

class Cliente(CRideModel):

	nombre = models.CharField('nombre cliente', max_length=50)
	apellido = models.CharField('apellido cliente', max_length=50)
	dpi = models.CharField(unique=True, max_length=13)
	telefono = models.CharField('telefono cliente', max_length=12)
	direccion = models.CharField('direccion cliente', max_length=100)

	def __str__(self):
		return self.nombre