"""Vista de maquinas"""

#Django REST Framework
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated

#Serializers
from maquinaria.maquinas.serializers import MaquinaModelSerializer

#Models
from maquinaria.maquinas.models import Maquina

class MaquinaViewSet(viewsets.ModelViewSet):

	queryset = Maquina.objects.all()
	serializer_class = MaquinaModelSerializer
	permission_classes = (IsAuthenticated,)