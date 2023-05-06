from django.shortcuts import render, redirect
from django.urls import reverse

from veterinaria.models import Animal, Doctor,Consultorio 
from veterinaria.forms import  AnimalFormulario

def presentar_home(request):
   
    http_responde = render(
        request=request,
        template_name='veterinaria/home.html',
    )
    return http_responde

def lista_animales(request):
    contexto = {
        "animales": Animal.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='veterinaria/lista_animales.html',
        context=contexto,
    )
    return http_response

def crear_animal(request):
    if request.method == "POST":
        formulario = AnimalFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  
            nombre = data["nombre"]
            raza = data["raza"]
            altura = data["altura"]
            peso = data["peso"]
            vacunado = data["vacunado"]
            dueño = data["dueño"]

            animal = Animal(nombre=nombre, raza=raza, altura = altura , peso = peso , vacunado = vacunado , dueño = dueño)  
            animal.save() 
          
            url_exitosa = reverse('lista_animales') 
            return redirect(url_exitosa)
    else:  # GET
        formulario = AnimalFormulario()
    http_response = render(
        request=request,
        template_name='veterinaria/formulario_animal.html',
        context={'formulario': formulario}
    )
    return http_response


def buscar_animales(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        animales = Animal.objects.filter(nombre__icontains=busqueda)
        contexto = {
            "animales": animales,
        }
        http_response = render(
            request=request,
            template_name='veterinaria/lista_animales.html',
            context=contexto,
        )
        return http_response