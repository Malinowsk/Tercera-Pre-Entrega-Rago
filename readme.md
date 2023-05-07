# Tercera Pre-Entrega ProyectoCoder 

## Resumen del proyecto

La web simula ser una veterinaria, tiene una base de datos con 3 tablas que son <strong>Animal</strong> , <strong>Doctor</strong> , <strong>Consultorio</strong> (más las tablas por defecto que trae django). Entrando a la raíz de la web nos encontramos con un home estático, en él podemos ver una barra de navegación que contiene un link hacia si mismo home y unos 3 links más que son (animales , doctores , consultorios). Estos 3 tienen la misma funcionalidad, cada uno relacionado con su tabla. Por ejemplo en animales ni bien entramos vemos la lista de todos los animales que contiene la tabla animal, también tenemos un buscar para buscar por nombre del animal, el cual al presional el boton de buscar nos va a redirigir al mismo link pero retringiendo los animales cuyo nombre contengan la palabra ingresada en el buscador. Además vemos un link que dice <strong>crear animal</strong> el cual nos lleva a una nueva página que contiene un formulario con todos los datos del animal para ingresar a la tabla correspondiente a Animal. Luego de llenar los datos y presionar el boton, si alguno de los datos ingresado no es válido nos vovlera al formulario mostrando el error que contiene alguno de los datos ingresados, por el ocntrario si ingresamos todo correctamente nos enviara nuevamente a la pagina donde vemos todo el listado de animales (el cual contendra el animal que ingresamos). Tanto para el link de doctores y consultorios se replica la misma logica.

## Instrucciones instalar proyecto en local
+ Instala el interprete de python en tu ordenador https://www.python.org/downloads/
+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre
+ Crea y activa el ambiente virtual
    + Ejecutar el comando: ```
python -m venv NOMBRECARPETA_VENV ```

    + Ejecutar el comando: ```
NOMBRECARPETA_VENV\Scripts\activate```
 (en cmd o powershell)
+ Clona este proyecto en la carpeta madre
    + Descarga git si no lo tienes en tu ordenador https://git-scm.com/downloads
    + Ejecutar el comando: ```git clone https://github.com/Malinowsk/Tercera-Pre-Entrega-Rago.git```
    + También existe la alternativa por SSH: ```git clone git@github.com:Malinowsk/Tercera-Pre-Entrega-Rago.git```
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```
+ Para instalar Django corre este comando:

```
pip install django
```

## Instrucciones para entrar al panel aministrativo de Django
+ En consola, crear un superuser:
```
python manage.py createsuperuser
```
+ Acceder con user y password via:
```
127.0.0.1:8000/admin
```


## Instrucciones para correr el proyecto web
+ En consola, ejecutar el comando:
```
python .\manage.py runserver
```
+ Ingresar desde el navegador web a la url:
```
127.0.0.1:8000/
```
