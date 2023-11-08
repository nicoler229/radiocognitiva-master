from django import forms
from .models import ParametrosIniciales
from .models import Archivos

class RangoFrecuenciasForm(forms.Form):
    class Meta:
        model = ParametrosIniciales
        frecuencia_inicial = forms.CharField(max_length=100)
        frecuencia_final = forms.CharField(max_length=100)

""" class SubirMP3Form(forms.Form):
    class Meta:
        model = Archivos
        fields = ['nombre', 'archivo']
        fields['archivo'] = forms.FileField(label='SUBIR ARCHIVO') """