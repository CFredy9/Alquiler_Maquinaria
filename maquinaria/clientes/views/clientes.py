"""Vista de maquinas"""

#Django REST Framework
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated

#Serializers
from maquinaria.clientes.serializers import ClienteModelSerializer

#Models
from maquinaria.clientes.models import Cliente

class ClienteViewSet(viewsets.ModelViewSet):

	queryset = Cliente.objects.all()
	serializer_class = ClienteModelSerializer
	permission_classes = (IsAuthenticated,)