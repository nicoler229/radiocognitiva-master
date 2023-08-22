from django.shortcuts import render
from django.shortcuts import redirect
from .models import Canales
from mutagen.mp3 import MP3



def post_list(request):
    return render(request, 'blog/post_list.html', {})

def home_view(request):
 
    return render(request, "home.html")

#PASO 1: ESTABLECER RANGO DE FRECUENCIA 
def establecer_rango(request):
    if request.method == 'POST':
        form = RangoFrecuenciasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver-rangos')
    else:
        form = forms.RangoFrecuenciasForm()
    
    return render(request, 'index.html', {'form': form})

def ver_rangos(request):
    rangos = RangoFrecuencias.objects.all()
    return render(request, 'index.html', {'rangos': rangos})

#def calcular_parametros(request):

def subir_mp3(request):
    if request.method == 'POST':
        form = SubirMP3Form(request.POST, request.FILES)
        if form.is_valid():
            archivo = form.cleaned_data['archivo_mp3']
            # Aquí puedes hacer lo que quieras con el archivo, como guardarlo en el servidor o en la base de datos
            return render(request, 'subir_mp3.html', {'form': form, 'mensaje': 'Archivo subido exitosamente'})
    else:
        form = UploadMP3Form()
    return render(request, 'subir_mp3.html', {'form': form})
      


#PASO 2: CORRER DETECTOR EN UN HILO PARA QUE ALMACENE DATA DE LOS CANALES DISPONIBLES EN LA BASE DE DATOS
def bloqueCognitivo(request):
    canales = Canales.objects.all()
    canal_seleccionado = null
    # Itera a través de los canales y obtén los valores que deseas
    for canal in canales:
        frecuencia = canal.frecuencia
        bandwidth = canal.bandwidth
        potencia = canal.potencia     

#PASO 3: OBTENER VALORES DESDE EL MODELO DE CANALES P
#PASO 4: CORRER BLOQUE COGNITIVO CON LA INFORMACION DE LOS CANALES Y ELEGIR EL MAS OPTIMO
#