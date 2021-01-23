"""User models admin"""
#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#Models
from maquinaria.usuarios.models import User

class CustomUserAdmin(UserAdmin):

	list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')

admin.site.register(User, CustomUserAdmin)