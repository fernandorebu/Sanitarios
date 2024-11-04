from centros import *

def test_leer_centros(archivo):
    datos =leer_centros(archivo)
    print(datos[:3])


def test_calcular_total_camas_centros_accesibles(CentroSanitaro):
    datos = calcular_total_camas_centros_accesibles(CentroSanitaro)
    print(datos)

if __name__ =='__main__':
    archivo ='data\centrosSanitarios.csv'
    CentroSanitaro = test_leer_centros(archivo)



    test_leer_centros(archivo)
    test_calcular_total_camas_centros_accesibles(CentroSanitaro)