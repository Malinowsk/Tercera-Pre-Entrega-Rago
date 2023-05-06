from django.contrib import admin
from django.urls import path

from veterinaria.views import presentar_home, lista_animales, crear_animal, buscar_animales

urlpatterns = [
    path("", presentar_home ,  name='home'),
    path("animales/", lista_animales ,  name='lista_animales'),
    path("crear-animal/", crear_animal ,  name='crear_animal'),
    path("buscar-animales/", buscar_animales ,  name='buscar_animales'),
    path("doctores", presentar_home ,  name='doctores'),
    path("consultorios", presentar_home ,  name='consultorios'),
]