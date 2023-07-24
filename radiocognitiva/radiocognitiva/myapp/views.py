from django.shortcuts import render
from django.shortcuts import render
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.http import HttpResponse
import io
import base64

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

def fft_view(request):
    # Generar señales de ejemplo para RX y TX
    fs = 1000  # Frecuencia de muestreo
    t = np.arange(0, 1, 1/fs)  # Vector de tiempo
    f1 = 10  # Frecuencia de la señal RX
    f2 = 15  # Frecuencia de la señal TX
    rx = np.sin(2*np.pi*f1*t)
    tx = np.sin(2*np.pi*f2*t)

    # Calcular la FFT de las señales
    RX = np.fft.fft(rx)
    TX = np.fft.fft(tx)
    freq = np.fft.fftfreq(len(rx), 1/fs)

    # Crear la ventana de gráfico
    fig, axes = plt.subplots(2, 1, figsize=(8, 6))

    # Graficar la FFT de RX
    axes[0].plot(freq, np.abs(RX))
    axes[0].set_xlabel('Frecuencia (Hz)')
    axes[0].set_ylabel('Magnitud')
    axes[0].set_title('Espectro de frecuencia RX')

    # Graficar la FFT de TX
    axes[1].plot(freq, np.abs(TX))
    axes[1].set_xlabel('Frecuencia (Hz)')
    axes[1].set_ylabel('Magnitud')
    axes[1].set_title('Espectro de frecuencia TX')

    # Guardar el gráfico en un buffer de memoria
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    # Renderizar la plantilla y pasar los datos del gráfico a la misma
    context = {'image_base64': image_base64}
    return render(request, "fft.html", context)