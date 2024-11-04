import csv
from coordenadas import Coordenadas
from collections import namedtuple

CentroSanitario = namedtuple('CentroSanitario', 'nombre, localidad, coordenadas,\
                              estado, num_camas, acceso_minusvalidos, tiene_uci')
def leer_centros(archivo):
    lista = []
    with open(archivo, encoding ="utf-8")as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)
        for nombre, localidad, latitud, longitud, estado, num_camas, acceso_minusvalidos, tiene_uci in lector:
            latitud = float(latitud)
            longitud = float(longitud)
            coordenadas = Coordenadas(latitud, longitud)
            num_camas = int(num_camas)
            acceso_minusvalidos = parsea_bool(acceso_minusvalidos)
            tiene_uci = parsea_bool(tiene_uci)
            lista.append(CentroSanitario(nombre, localidad, coordenadas, estado, num_camas, acceso_minusvalidos, tiene_uci))
    return lista


def parsea_bool(valor):
    res = 0
    if valor == 'true':
        res = True
    else:
        res = False
    return res


def calcular_total_camas_centros_accesibles(CentroSanitaro):
    numero_camas = 0
    for centro in CentroSanitaro:
        if centro.acceso_minusvalidos == True:
            numero_camas += centro.num_camas
    return numero_camas
