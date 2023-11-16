from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('sucursales/', views.sucursales, name='sucursales')
]