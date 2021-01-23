"""Serializers Alquileres"""

#Django REST Framework
from rest_framework import serializers 

#Model
from maquinaria.alquileres.models import Alquiler
from maquinaria.maquinas.models import Maquina

class AlquilerModelSerializer(serializers.ModelSerializer):
	"""Modelo Serializer de Cliente"""

	class Meta:
		"""Clase Meta"""
		model = Alquiler
		fields = (
			'id', 'cliente', 
			'maquina', 'fecha_inicio', 
			'fecha_final', 'precio_alquiler'
			)

class Update(serializers.Serializer):

	def save(self):
		maquina=Maquina.objects.get(id=1)
		maquina.estado=False
		maquina.save()
		
	




				