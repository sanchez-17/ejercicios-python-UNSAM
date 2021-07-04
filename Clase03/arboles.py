# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 13:31:30 2021

@author: Gaston
"""
import csv
from pprint import pprint


nombre_archivo = "../Data/arbolado-en-espacios-verdes.csv"

def leer_parque(nombre_archivo, parque):
    arbolado = []
    with open(nombre_archivo, 'rt', encoding = 'utf-8') as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                data = dict( zip(headers, row))
                if data['espacio_ve'] == parque:
                    data['altura_tot'] = float( data['altura_tot'] )
                    arbolado.append(data)
    return arbolado
            
parque1 = leer_parque(nombre_archivo, 'GENERAL PAZ')
#%%
'''
Ejercicio 3.19
'''
def especies(lista_arboles):
    data = []
    for row in lista_arboles:
        data.append(row['nombre_com'])
    return set(data)

pprint( especies(parque1) )
#%%
'''
Ejercicio 3.20
'''
from collections import Counter

def contar_ejemplares(lista_arboles):
    lista = []
    for s in lista_arboles:
        lista.append(s['nombre_com'])
    total = Counter(lista)
    return total

parque2 = leer_parque(nombre_archivo, 'ANDES, LOS')
parque3 = leer_parque(nombre_archivo, 'CENTENARIO')

pprint(contar_ejemplares(parque1).most_common(5))
pprint(contar_ejemplares(parque2).most_common(5))
pprint(contar_ejemplares(parque3).most_common(5))

#%%
'''
Ejercicio 3.21
'''

def obtener_alturas(lista_arboles, especie):
    lista = []
    for s in lista_arboles:
        if s['nombre_com'] == especie :
            lista.append(s['altura_tot'])
    return lista

'''
Imprimo resultados de maxima y media
'''

from statistics import mean

alturas_lista = [obtener_alturas(parque1, 'Jacarandá'),
     obtener_alturas(parque2, 'Jacarandá'),
     obtener_alturas(parque3, 'Jacarandá')
     ]
parques = ['General Paz', 'Los Andes', 'Centenario']

print('Medida', end='')
for i in parques:
    print(f'     {i:s}', end='')
print()

print('Max |', end='')
for i in alturas_lista:
    print(f'{max(i):>15}', end='')
print()

print('Prom|', end='')
for s in alturas_lista:
    print(f'{mean(s):>15.02f}', end='')

#%%
'''
Ejercicio 3.22
'''

def obtener_inclinaciones(lista_arboles, especie):
    lista = []
    for i in lista_arboles:
        if i['nombre_com'] == especie:
            lista.append(float( i['inclinacio']) )
    return lista

# a = obtener_inclinaciones(parque1, 'Jacarandá')

#%%
'''
Ejercicio 3.23
'''

def especimen_mas_inclinado(lista_arboles):
    lista_especies = especies(lista_arboles)
    a = []
    for s in lista_especies:
        d = max(obtener_inclinaciones(lista_arboles, s))
        a.append( (d,s) )
    ejemplar_mas_inclinado = max(a)
    
    return ejemplar_mas_inclinado

# b = especimen_mas_inclinado(parque3)
    
#%%
'''
Ejercicio 3.24
'''

def especie_promedio_mas_inclinada(lista_arboles):
    lista_especies = especies(lista_arboles)
    a = []
    for especie in lista_especies:
        d = obtener_inclinaciones(lista_arboles, especie)
        a.append( (mean(d),especie) )
    especie_mas_inclinada = max(a)
    
    return especie_mas_inclinada

# b = especie_promedio_mas_inclinada(parque2)
# print(b)