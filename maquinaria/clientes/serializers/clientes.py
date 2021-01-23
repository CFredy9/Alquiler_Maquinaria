"""Serializers clientes"""

#Django REST Framework
from rest_framework import serializers 

#Model
from maquinaria.clientes.models import Cliente

class ClienteModelSerializer(serializers.ModelSerializer):
	"""Modelo Serializer de Cliente"""

	class Meta:
		"""Clase Meta"""
		model = Cliente
		fields = (
			'id', 'nombre', 
			'apellido', 'dpi', 
			'telefono', 'direccion'
			)