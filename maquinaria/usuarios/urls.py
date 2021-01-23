"""URls de Usuarios"""

#Django
from django.urls import path 

#Views
from maquinaria.usuarios.views import (
	UserLoginAPIView, 
	UserSignUpAPIView
	) 

urlpatterns = [
	path('usuarios/login/', UserLoginAPIView.as_view(), name='login'),
	path('usuarios/signup/', UserSignUpAPIView.as_view(), name='signup'),
]
