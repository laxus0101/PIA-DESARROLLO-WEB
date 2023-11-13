from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def medicos (request):
    return HttpResponse("<h1>Bienvenido a sitio de Medicos</h1>")
def index(request):
    return HttpResponse("<h1>Bienvenido al menu de sucursales</h1>")