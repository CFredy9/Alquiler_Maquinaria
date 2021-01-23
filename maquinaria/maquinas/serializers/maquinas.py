"""Serializers maquinas"""

#Django REST Framework
from rest_framework import serializers 

#Model
from maquinaria.maquinas.models import Maquina

class MaquinaModelSerializer(serializers.ModelSerializer):
	"""Modelo Serializer de Maquina"""

	class Meta:
		"""Clase Meta"""
		model = Maquina
		fields = (
			'id', 'nombre', 'nombre_clave', 
			'peso', 'estado', 'descripcion',
			)