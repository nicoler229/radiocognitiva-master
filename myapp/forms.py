from django import forms
from .models import ParametrosIniciales

class RangoFrecuenciasForm(forms.ParametrosIniciales):
    class Meta:
        model = ParametrosIniciales
        fields = ['frecuencia_inicial', 'frecuencia_final']

class SubirMP3Form(forms.Form):
    archivo_mp3 = forms.FileField(label='SUBIR ARCHIVO')