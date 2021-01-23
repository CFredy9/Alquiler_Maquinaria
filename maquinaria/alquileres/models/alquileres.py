"""Modelo de Alquileres"""

#Django
from django.db import models
from django.utils import timezone


#Utilities
from maquinaria.utils.models import CRideModel

from maquinaria.maquinas.models import Maquina


from datetime import datetime
from datetime import timedelta


class Alquiler(CRideModel):

	cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
	maquina = models.ForeignKey('maquinas.Maquina', on_delete=models.CASCADE)
	#fecha_inicio = models.DateTimeField(auto_now_add=True)
	fecha_inicio = models.DateTimeField(auto_now_add=True)
	fecha_final = timezone.now() + timedelta(days=1)
	precio_alquiler = models.IntegerField()

	


	def __str__(self):
		return self.cliente