"""Vista de alquileres"""

#Django REST Framework
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.views import APIView

#Serializers
from maquinaria.alquileres.serializers import AlquilerModelSerializer, Update

#Models
from maquinaria.alquileres.models import Alquiler
from maquinaria.maquinas.models import Maquina

class AlquilerViewSet(viewsets.ModelViewSet):

	queryset = Alquiler.objects.all()
	serializer_class = AlquilerModelSerializer
	permission_classes = (IsAuthenticated,)

	
class Estado(APIView):

	def post(self, request, *args, **kwargs):
		serializer = Update(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		data = {'message': 'Estado de maquina cambiado'}
		return Response(data, status=status.HTTP_200_OK)






"""maquina=Maquina.objects.get(id=4)
		maquina.estado=False
		maquina.save()"""

	
