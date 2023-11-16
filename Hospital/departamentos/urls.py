from django.urls import path
from . import views

urlpatterns=[
    path('departamentos/', views.departamentos, name='departamentos')
]