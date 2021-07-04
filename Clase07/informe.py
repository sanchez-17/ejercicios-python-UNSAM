# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 12:19:44 2021

@author: Gaston
"""
from fileparse import parse_csv
import sys

def leer_camion(nombre_archivo):
    with open(nombre_archivo) as f:
        d = parse_csv(f, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    return d

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        d = parse_csv(f, types = [str, float], has_headers = False)
    return dict(d)

def balance(nombre_camion, nombre_precios):
    #Instancio los valores para los costos y leo los archivos del camion y la lista de precios
    camion = leer_camion(nombre_camion)
    precio = leer_precios(nombre_precios)
    costo_camion = 0
    costo_venta = 0
    #Calcula el costo del camion y estima la venta de los productos existentes en el camion
    for cajon in camion:
        try:
            costo_camion += cajon['cajones'] * cajon['precio']
            costo_venta += cajon['cajones'] *  precio[ cajon['nombre'] ] 
        except:
            #Si un lote no tiene precio de venta lo agrega a una lista y no se toma en cuenta en la venta
            lista_frutas_sin_precio = []
            lista_frutas_sin_precio.append(cajon['nombre'])
            continue
    res = costo_venta - costo_camion
    print(f'\nBalance: ${res:0.2f}\n')
    return res

def hacer_informe(camion, precios):

    salida = []
    for i in camion:
        try:
            salida.append( (i['nombre'], i['cajones'], precios[i['nombre']] , precios[i['nombre']] - i['precio']))
        except KeyError:
            pass
    return salida

def preparar_informe(archivo_camion , archivo_precios):
    
    lista_camion = leer_camion(archivo_camion)
    lista_precios = leer_precios(archivo_precios)
    
    informe = hacer_informe(lista_camion, lista_precios)
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    
    return informe, headers

def imprimir_informe(informe):
    info, headers = informe
    
    for head in headers:
        print(f'{head:>10s} ', end='')
    print()
    print(f'---------- ' * len(headers))
    
    for nombre, cajones, precio, cambio in info:
        precio_aux = f'${round(precio,2)}'
        print(f'{nombre:>10s} {cajones:>10d} {precio_aux:>10s} {cambio:>10.2f}')


def informe_camion(archivo_camion, archivo_precios):
    informe = preparar_informe(archivo_camion, archivo_precios)
    imprimir_informe(informe)

def main(argv):
    if len(argv) != 3:
        print(f'Uso correcto: \n{argv[0]} CAMION PRECIOS')
    else:
        archivo_camion = argv[1]
        archivo_precios = argv[2]
        informe_camion(archivo_camion, archivo_precios)
    
if __name__ == '__main__':
    import sys
    main(sys.argv)
    
# '../Data/camion.csv', '../Data/precios.csv'
