from django.db.models import Avg, Max, Min, Sum


from rest_framework.decorators import api_view
from django.http import HttpResponse

#Django REST Framework
from rest_framework import viewsets 

from maquinaria.alquileres.models import Alquiler
from maquinaria.clientes.models import Cliente

def Reporte(request):

	Total = Alquiler.objects.all()
	cliente = Cliente.objects.filter(id=1)
	return HttpResponse(Cliente)