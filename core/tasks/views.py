import string

from django.shortcuts import render
from django.utils.crypto import get_random_string

from django.contrib.auth.models import User

# Create your views here.

def create_random_user(quantity):
    for x in range(quantity):
        username = f'usario_{get_random_string(5,string.ascii_letters)}'
        email = f'{username}@miempresa.pe'
        password = get_random_string(50)

        User.objects.create_user(username=username, email=email, password=password)
    return f'{quantity} Usuarios creados correctamente.'

