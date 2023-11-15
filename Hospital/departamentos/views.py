from django.shortcuts import render
from django.http import HttpResponse
from .models import departamentos

# Create your views here.
def departamentos (request):
    return HttpResponse("<h1>Bienvenido a sitio de departamentos</h1>")
def index(request):
    return HttpResponse("<h1>Bienvenido al menu de sucursales</h1>")