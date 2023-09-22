from django.shortcuts import render
from django.shortcuts import redirect
from .models import Canales
from mutagen.mp3 import MP3
from .forms import RangoFrecuenciasForm



def post_list(request):
    return render(request, 'blog/post_list.html', {})

def home_view(request):
 
    return render(request, "vista.html")

#PASO 1: ESTABLECER RANGO DE FRECUENCIA 
def establecer_rango(request):
    if request.method == 'POST':
        form = RangoFrecuenciasForm(request.POST)
        if form.is_valid():
            frecuencia_inicial = form.cleaned_data['frecuencia_inicial']
            frecuencia_final = form.cleaned_data['frecuencia_final']
            form.save()
            return redirect('ver-rangos')
    else:
        form = RangoFrecuenciasForm()
    
    return render(request, 'vista.html', {'form': form})

def ver_rangos(request):
    rangos = RangoFrecuencias.objects.all()
    return render(request, 'index.html', {'rangos': rangos})

#SUBIR ARCHIVO MP3
def subir_mp3(request):
    if request.method == 'POST':
        form = SubirMP3Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            archivo = form.cleaned_data['archivo_mp3']
            # Aquí puedes hacer lo que quieras con el archivo, como guardarlo en el servidor o en la base de datos
            return render(request, 'subir_mp3.html', {'form': form, 'mensaje': 'Archivo subido exitosamente'})
    else:
        form = UploadMP3Form()
    return render(request, 'subir_mp3.html', {'form': form})

def anchoDeBandaMp3():
    archivo_mp3 = Archivos.objects.last() #ultimo archivo subido
    info_mp3 = MP3(archivo_mp3)
    tasa_bits_audio = info_mp3.info.bitrate
    numero_simbolos_por_segundo = 1000
    ancho_banda_necesario = tasa_bits_audio / numero_simbolos_por_segundo
    print(f"Ancho de Banda Necesario: {ancho_banda_necesario:.2f} Hz")
    return ancho_banda_necesario

def calcular_snr_min(capacidad, ancho_de_banda_minimo):
    snr_min = capacidad / bandwidth
    return snr_min



#PASO 2: CORRER DETECTOR EN UN HILO PARA QUE ALMACENE DATA DE LOS CANALES DISPONIBLES EN LA BASE DE DATOS
def bloqueCognitivo(request):
    canales = Canales.objects.all()
    canal_seleccionado = none 
    mejor_puntuacion = float('-inf')
    ancho_de_banda_minimo = anchoDeBandaMp3()
    capacidad = 1000
    potencia_maxima = -70
    snr_min = calcular_snr_min(capacidad, ancho_de_banda_minimo)
    print(f"SNR mínimo requerido: {snr_min:.2f} dB")
    #PASO 3: OBTENER VALORES DESDE EL MODELO DE CANALES P
    for canal in canales:
        frecuencia = canal.frecuencia
        ancho_banda_suficiente = canal.bandwith >= ancho_de_banda_minimo
        snr_aceptable = canal.snr >= snr_minimo
        potencia_baja = canal.potencia <= potencia_maxima
        puntuacion = ancho_banda_suficiente + snr_aceptable + (1 / potencia_baja)

        if puntuacion > mejor_puntuacion:
                mejor_puntuacion = puntuacion
                mejor_espacio = canal

        return mejor_espacio


# Definir los valores mínimos para cada parámetro
#ancho_banda_minimo_mp3 = 128  # kbps
#snr_minimo = 10  # dB
  # dBm

#PASO 4: CORRER BLOQUE COGNITIVO CON LA INFORMACION DE LOS CANALES Y ELEGIR EL MAS OPTIMO
