# -*- coding: utf-8 -*-

from vigilante import vigilar
import csv

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]
        
def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

if __name__ == '__main__':
    lines = vigilar('../Data/mercadolog.csv')
    rows = parsear_datos(lines)
    for row in rows:
        print(row)
        
#%%
        
import informe
camion = informe.leer_camion('../Data/camion.csv')
filas = parsear_datos(vigilar('../Data/mercadolog.csv'))
filas = filtrar_datos(filas, camion)
for fila in filas:
    print(fila)
    
#%%
    
''' Ejercicio 10.12'''
import formato_tabla

def ticker(camion_file, log_file, fmt):
    camion = informe.leer_camion(camion_file)
    rows = parsear_datos(vigilar(log_file))
    
    formateador = formato_tabla.crear_formateador(fmt)
    formateador.encabezado(['nombre', 'precio','volumen'])
    
    rows = (row for row in rows if row['nombre'] in camion )
    
    for row in rows:
        precio= row['precio']
        rowdata = [ row['nombre'],f'{precio:0.2f}',str(row['volumen']) ]
        formateador.fila(rowdata)
