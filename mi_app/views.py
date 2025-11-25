from django.shortcuts import render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import HttpResponse
import re


def formulario_view(request):
	"""Renderiza el formulario y procesa envíos POST con validación básica."""
	if request.method == 'POST':
		nombre = request.POST.get('nombre', '').strip()
		apellidos = request.POST.get('apellidos', '').strip()
		email = request.POST.get('email', '').strip()
		password = request.POST.get('password', '')
		telefono = request.POST.get('telefono', '').strip()
		nacimiento = request.POST.get('nacimiento', '').strip()
		direccion = request.POST.get('direccion', '').strip()

		errors = {}

		# Validar correo
		try:
			validate_email(email)
		except ValidationError:
			errors['email'] = 'Introduce un correo electrónico válido.'

		# Validar contraseña: mínimo 8, al menos una mayúscula y un número
		if not password:
			errors['password'] = 'La contraseña es obligatoria.'
		else:
			if len(password) < 8 or not re.search(r'[A-Z]', password) or not re.search(r'\d', password):
				errors['password'] = 'La contraseña debe tener al menos 8 caracteres, incluir una mayúscula y un número.'

		if errors:
			context = {
				'errors': errors,
				'data': request.POST,
			}
			return render(request, 'mi_app/formulario.html', context)

		# Aquí podrías crear un usuario o guardar datos en la base
		context = {'nombre': nombre}
		return render(request, 'mi_app/exito.html', context)

	# GET
	return render(request, 'mi_app/formulario.html')


def exito_view(request):
	return render(request, 'mi_app/exito.html')
