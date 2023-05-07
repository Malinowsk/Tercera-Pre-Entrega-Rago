from django import forms


class AnimalFormulario(forms.Form):
    nombre = forms.CharField(max_length=256,required=True)
    raza = forms.CharField( label='Raza', max_length=256,required=True)
    altura = forms.DecimalField(max_digits=7, decimal_places=2)
    peso = forms.DecimalField(max_digits=7, decimal_places=2)
    vacunado = forms.BooleanField(required=False)
    dueño = forms.CharField(max_length=256,required=True)


class DoctorFormulario(forms.Form):
    apellido = forms.CharField(max_length=256,required=True)
    nombre = forms.CharField(max_length=256,required=True)
    dni = forms.CharField(max_length=32,required=True)
    email = forms.EmailField(required=True)
    puesto = forms.CharField(max_length=128,required=True)


class ConsultorioFormulario(forms.Form):
    nombre = forms.CharField(max_length=256,required=True)
    num_piso = forms.CharField(max_length=32,required=True)
    metros_cuadrados = forms.DecimalField(max_digits=7, decimal_places=2)
    con_tetoscopio = forms.BooleanField(required=False)
