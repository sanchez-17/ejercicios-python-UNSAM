# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 03:18:57 2021

@author: Gaston
"""
import csv
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

H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

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