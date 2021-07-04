# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 03:18:57 2021

@author: Gaston
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
# import random
# from pprint import pprint


'''
Ejercicio 4.15
'''

def leer_arboles(nombre_archivo):
    f = open(nombre_archivo, 'rt', encoding = 'utf-8')
    rows = csv.reader(f)
    headers = next(rows)
    indices = [headers.index(ncolumna) for ncolumna in headers]
    arboleda = [{ ncolumna: row[index] for ncolumna, index in zip(headers, indices)} for row in rows]
    f.close()
    return arboleda


nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'

arboleda = leer_arboles(nombre_archivo)

#%%

'''
Ejercicio 4.16
'''

alturas_jac=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
alturas_jac = np.array(alturas_jac)
#%%

'''
Ejercicio 4.17
'''

pares = [ ( float(arbol['altura_tot']) , float(arbol['diametro']) ) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá' ]

#%%

'''
Ejercicio 4.18
'''

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

def medidas_de_especies(especies,arboleda):
    diccionario = { especie : [ ( float(arbol['altura_tot']) , float(arbol['diametro']) ) for arbol in arboleda if arbol['nombre_com'] == especie ] for especie in especies }
    return diccionario

a = medidas_de_especies(especies,arboleda)
# a = np.array(a)
#%%
'''Ejercicio 5.24'''

plt.hist(alturas_jac, bins = 5)
plt.xlabel("Altura en cm")
plt.ylabel("Ocurrencias")
plt.title("Altura de Jacarandás")

#%%
'''Ejercicio 5.25'''

alt = np.array(pares)[:,0]
diam = np.array(pares)[:,1]

N = len(pares)
colors = np.random.rand(N)

plt.scatter( diam , alt , c = colors, alpha = .3, s = 20* (diam/alt))
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")

#%%
'''Ejercicio 5.26'''

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

for i in especies:
    h = np.array(a[i])[:,0]
    d = np.array(a[i])[:,1]
    plt.scatter( d , h ,alpha = .5 , s = 5 )
    
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para 3 especies diferentes")

# plt.xlim(0,30) 
# plt.ylim(0,100) 