from django.contrib import admin
from django.urls import path

from veterinaria.views import presentar_home, lista_animales, crear_animal, buscar_animales, lista_doctores, crear_doctor, buscar_doctores,lista_consultorios, crear_consultorio, buscar_consultorios 

urlpatterns = [
    path("", presentar_home ,  name='home'),
    path("animales/", lista_animales ,  name='lista_animales'),
    path("crear-animal/", crear_animal ,  name='crear_animal'),
    path("buscar-animales/", buscar_animales ,  name='buscar_animales'),

    path("doctores/", lista_doctores ,  name='lista_doctores'),
    path("crear-doctor/", crear_doctor ,  name='crear_doctor'),
    path("buscar-doctores/", buscar_doctores ,  name='buscar_doctores'),

    path("consultorios/", lista_consultorios ,  name='lista_consultorios'),
    path("crear-consultorio/", crear_consultorio ,  name='crear_consultorio'),
    path("buscar-consultorios/", buscar_consultorios ,  name='buscar_consultorios'),

]