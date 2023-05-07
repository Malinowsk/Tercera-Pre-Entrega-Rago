from django.shortcuts import render, redirect
from django.urls import reverse

from veterinaria.models import Animal, Doctor,Consultorio 
from veterinaria.forms import  AnimalFormulario , DoctorFormulario , ConsultorioFormulario

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
    


def lista_doctores(request):
    contexto = {
        "doctores": Doctor.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='veterinaria/lista_doctores.html',
        context=contexto,
    )
    return http_response

def crear_doctor(request):
    if request.method == "POST":
        formulario = DoctorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  
            nombre = data["nombre"]
            apellido = data["apellido"]
            dni = data["dni"]
            email = data["email"]
            puesto = data["puesto"]

            doctor = Doctor(nombre=nombre, apellido=apellido, dni = dni , email = email , puesto = puesto )  
            doctor.save() 
          
            url_exitosa = reverse('lista_doctores') 
            return redirect(url_exitosa)
    else:  # GET
        formulario = DoctorFormulario()
    http_response = render(
        request=request,
        template_name='veterinaria/formulario_doctor.html',
        context={'formulario': formulario}
    )
    return http_response


def buscar_doctores(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        doctores = Doctor.objects.filter(nombre__icontains=busqueda)
        contexto = {
            "doctores": doctores,
        }
        http_response = render(
            request=request,
            template_name='veterinaria/lista_doctores.html',
            context=contexto,
        )
        return http_response


def lista_consultorios(request):
    contexto = {
        "consultorios": Consultorio.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='veterinaria/lista_consultorios.html',
        context=contexto,
    )
    return http_response

def crear_consultorio(request):
    if request.method == "POST":
        formulario = ConsultorioFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  
            nombre = data["nombre"]
            num_piso = data["num_piso"]
            metros_cuadrados = data["metros_cuadrados"]
            con_tetoscopio = data["con_tetoscopio"]

            consultorio = Consultorio(nombre=nombre, num_piso=num_piso, metros_cuadrados = metros_cuadrados , con_tetoscopio = con_tetoscopio)  
            consultorio.save() 
          
            url_exitosa = reverse('lista_consultorios') 
            return redirect(url_exitosa)
    else:  # GET
        formulario = ConsultorioFormulario()
    http_response = render(
        request=request,
        template_name='veterinaria/formulario_consultorio.html',
        context={'formulario': formulario}
    )
    return http_response


def buscar_consultorios(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        consultorios = Consultorio.objects.filter(nombre__icontains=busqueda)
        contexto = {
            "consultorios": consultorios,
        }
        http_response = render(
            request=request,
            template_name='veterinaria/lista_consultorios.html',
            context=contexto,
        )
        return http_response