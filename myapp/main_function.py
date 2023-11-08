# Crear una lista de espacios en blanco con ancho de banda, SNR y potencia
from models import Canales
from views import bloqueCognitivo

def correr():
    
    espacios = Canales.object.all()

    # Crear un bloque cognitivo y evaluar los espacios en blanco
    espacio_seleccionado = bloqueCognitivo(espacios)

    print("Mejor espacio en blanco:")
    print("Frecuencia del espacio:", espacio_seleccionado.frecuencia)
    
    
    