from django.shortcuts import render
from django.http import HttpResponse
from .models import Sucursalesinfo
# Create your views here.
def index(request):
    #obtener los datos 
    data = Sucursalesinfo.objects.all()
    info = {
        "datos": data
    }
    return render(request,"index.html", context=info)



