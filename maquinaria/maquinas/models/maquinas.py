"""Modelo de maquina"""

#Django
from django.db import models

#Django REST Framework
#from rest_framework.validators import UniqueValidator

#Utilities
from maquinaria.utils.models import CRideModel

class Maquina(CRideModel):
	"""Un circulo es un grupo privado"""

	nombre = models.CharField('nombre maquina', max_length=50)
	nombre_clave = models.CharField('nombre clave', unique=True, max_length=40)
	peso = models.CharField('peso', max_length=255)
	estado = models.BooleanField('estado', default=True)
	descripcion = models.CharField('descripcion', blank=True, max_length=100)
	

	"""members = models.ManyToManyField(
		'users.User', 
		through='circles.Membership',
		through_fields=('circle', 'user')
		) """
	

	"""verified = models.BooleanField(
		'verified circle', 
		default=False, 
		help_text='Verified circles are also know  as official comunities'
		) """

	

	def __str__(self):
		return self.name

	class Meta(CRideModel.Meta):
		"""Meta class"""

		#ordering = ['-rides_taken', '-rides_offered']