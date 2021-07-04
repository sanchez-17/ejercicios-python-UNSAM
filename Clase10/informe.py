# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 12:19:44 2021

@author: Gaston
"""
from fileparse import parse_csv
import lote
import sys
import formato_tabla
from camion import Camion

def leer_camion(nombre_archivo):
    '''
    Lee un archivo con el contenido de un camión
    y lo devuelve como un objeto Camion.
    '''
    with open(nombre_archivo) as f:
        camion_dicts = parse_csv(f, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
        camion = [ lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return Camion(camion)

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
            salida.append( (i.nombre, i.cajones, precios[i.nombre] , precios[i.nombre] - i.precio))
        except KeyError:
            pass
    return salida


def imprimir_informe(informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas con (nombre, cajones, precio, cambio) 
    '''
    # headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    
    # print('%10s %10s %10s %10s' % headers)
    # print( ('-'*10 +' ') * len(headers))
    
    # for nombre, cajones, precio, cambio in informe:
    # #for row in informe:
    #     precio_aux = f'${precio}'
    #     #print('%10s %10d $%10.2f %10.2f' % row)
    #     print(f'{nombre:>10s} {cajones:>10d} {precio_aux:>10s} {cambio:>10.2f}')
    
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in informe:
        rowdata = [ nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}' ]
        formateador.fila(rowdata)


def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es txt
    Alternativas: csv o html
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)
    
    # Obtener los datos para el informe
    data_informe = hacer_informe(camion, precios)
    
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)
    
    



def main(argv):
    if len(argv) == 3 :
        archivo_camion = argv[1]
        archivo_precios = argv[2]
        informe_camion(archivo_camion, archivo_precios)
    elif len(argv) == 4:
        archivo_camion = argv[1]
        archivo_precios = argv[2]
        formato = argv[3]
        informe_camion(archivo_camion, archivo_precios, formato)
    else:
        print(f'Uso correcto: \n{argv[0]} CAMION PRECIOS FORMATO(opcional')
    
if __name__ == '__main__':
    import sys
    main(sys.argv)
    
# '../Data/camion.csv', '../Data/precios.csv'
