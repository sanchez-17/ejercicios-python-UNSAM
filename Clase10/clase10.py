# -*- coding: utf-8 -*-
"""
Created on Wed May 26 02:18:17 2021

@author: Gaston
"""
from vigilante import vigilar
'''
Ejercicio 10.8
'''
def filematch(lines, substr):
        for line in lines:
            if substr in line:
                yield line

#%%
                
lines = vigilar('../Data/mercadolog.csv')
naranjas = filematch(lines, 'Naranja')
for line in naranjas:
    print(line)
#%%
'''Ejercicio 10.9'''

import csv
lineas = vigilar('../Data/mercadolog.csv')
filas = csv.reader(lineas)
for fila in filas:
    print(fila)
