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

def index(request):
    return render(request,"index.html")

def sucursales(request):
<<<<<<< HEAD
    return render(request,"sucursales.html")


=======
    return HttpResponse("<h1>Bienvenido al hospital</h1>")
>>>>>>> 0427a346f88c86189d5c71ff6f82763ad738f8c4
