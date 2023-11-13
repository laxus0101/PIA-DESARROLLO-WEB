from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sucursales(request):
    return HttpResponse("<h1>Bienvenido al hospital</h1>")

def index(request):
    return HttpResponse("<h1>Bienvenido al menu de sucursales</h1>")