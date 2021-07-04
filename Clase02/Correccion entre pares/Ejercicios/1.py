# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 16:18:19 2021

@author: matye

Ejercicio 2.18: Balances
Supongamos que los precios en camion.csv son los precios
pagados al productor de frutas mientras que los precios en
precios.csv son los precios de venta en el lugar de descarga
del camión.

Ahora vamos calcular el balance del negocio: juntá todo el 
trabajo que hiciste recién en tu programa informe.py (usando 
las funciones leer_camion() y leer_precios()) y completá el
programa para que con los precios del camión (Ejercicio 2.16)
y los de venta en el negocio (Ejercicio 2.17) calcule lo que 
costó el camión, lo que se recaudó con la venta, y la diferencia
¿Hubo ganancia o pérdida? El programa debe imprimir por
pantalla un balance con estos datos.
"""

import csv

def leer_precios(file):
    with open(file, 'rt') as f:
        rows = csv.reader(f)
        precios = {}
        for row in rows:
            try:
                precios[row[0]] = float(row[1])
                
            except: 
                pass
            
    return precios

def leer_camion(file):
    with open(file, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        camion = []
        dic = {}
        for row in rows:
            try:
                camion.append({
                    'nombre': row[0],
                    'cajones': int(row[1]),
                    'precio': float(row[2])
                    })
            except: 
                pass
            
    return camion

precios = leer_precios('../Data/precios.csv')
camion = leer_camion('../Data/camion.csv')

balance = 0

for i in camion:
    parcial = i['cajones'] * (precios[i['nombre']]  - i['precio'])
    balance += parcial
    
print(f'El balance entre el costo total y la recaudacion fue: ${balance}')