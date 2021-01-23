"""Users serializers"""

#Django
from django.conf import settings 
from django.contrib.auth import password_validation, authenticate
from django.core.mail import EmailMultiAlternatives
from django.core.validators import RegexValidator
from django.template.loader import render_to_string
from django.utils import timezone

#Django REST Framework
from rest_framework import serializers

from rest_framework.authtoken.models import Token 
from rest_framework.validators import UniqueValidator

#Models
from maquinaria.usuarios.models import User

#Utilities
import jwt 
from datetime import timedelta

class UserModelSerializer(serializers.ModelSerializer):
	"""User model serializer"""

	class Meta:

		model = User 
		fields = (
			'username', 
			'first_name', 
			'last_name', 
			'email', 
			'phone_number',
			)

class UserSignUpSerializer(serializers.Serializer):
	"""User sign up serializer"""

	email = serializers.EmailField(
		validators=[UniqueValidator(queryset=User.objects.all())]
		)
	username = serializers.CharField(
		min_length=4, 
		max_length=20,
		validators=[UniqueValidator(queryset=User.objects.all())]
		)
	#Phone number
	phone_regex = RegexValidator(
		regex=r'\+?1?\d{9,15}$', 
		message='Phone number must be entered in the format: +999999999 Up to 15 digits allowed'
		)
	phone_number = serializers.CharField(validators=[phone_regex])
	#password
	password = serializers.CharField(min_length=8, max_length=64)
	password_confirmation = serializers.CharField(min_length=8, max_length=64)
	#Name
	first_name = serializers.CharField(min_length=2, max_length=30)
	last_name = serializers.CharField(min_length=2, max_length=30)

	def validate(self, data):
		"""Verify passwords match"""
		passwd = data['password']
		passwd_conf = data['password_confirmation']
		if passwd != passwd_conf:
			raise serializers.ValidationError('Passwords does not mach')
		password_validation.validate_password(passwd)
		return data

	def create(self, data):

		data.pop('password_confirmation')
		user = User.objects.create_user(**data)
		#self.send_confirmation_email(user)
		return user


	def gen_verification_token(self, user):
		"""Create JWT token that the user can use to verify its account"""
		exp_date = timezone.now() + timedelta(days=3)
		payload = {
			'user': user.username,
			'exp': int(exp_date.timestamp()),
			'type': 'email_confirmation'
		}
		token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
		return Response(token) 

class UserLoginSerializer(serializers.Serializer):
	"""User Login serializer"""

	#email = serializers.EmailField()
	username = serializers.CharField(min_length=4, max_length=20)
	password = serializers.CharField(min_length=8, max_length=64)

	def validate(self, data):
		"""Check credentials"""
		user = authenticate(username=data['username'], password=data['password'])
		if not user:
			raise serializers.ValidationError('Invalid credentials')
		if not user.is_verified:
			raise serializers.ValidationError('Account is not active yet :(')
		self.context['user'] = user
		return data

	def create(self, data):
		"""Generate or retrieve new token"""
		token, created = Token.objects.get_or_create(user=self.context['user']) 
		return self.context['user'], token.key