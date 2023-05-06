from django import forms


class AnimalFormulario(forms.Form):
    nombre = forms.CharField(max_length=256,required=True)
    raza = forms.CharField(max_length=256,required=True)
    altura = forms.DecimalField(max_digits=7, decimal_places=2)
    peso = forms.DecimalField(max_digits=7, decimal_places=2)
    vacunado = forms.BooleanField(required=False)
    dueño = forms.CharField(max_length=256,required=True)

