from collections import namedtuple
import math

Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')
'''
def calcular_distancia(coordenada1, coordenada2):
    primer_termino = (coordenada1[0] + coordenada2[0]) ** 2
    segundo_termino = (coordenada1[1] + coordenada2[1]) ** 2
    raiz_cuadrada = math.sqrt(primer_termino + segundo_termino)
    return raiz_cuadrada
'''
def calcular_distancia(coordenada1, coordenada2):
    return math.sqrt((coordenada1.latitud-coordenada2.latitud)**2 + (coordenada1.longitud-coordenada2.longitud)**2)


def calcular_media_coordenadas(Coordenadasss):
    suma_lat = []
    suma_lon = []
    for latitud, longitud in Coordenadasss:
        suma_lat.append(latitud)
        suma_lon.append(longitud)
    return Coordenadas(sum(suma_lat)/len(suma_lat), sum(suma_lon)/len(suma_lon))


    

