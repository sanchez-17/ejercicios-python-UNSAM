# -*- coding: utf-8 -*-
"""
Created on Wed May 12 01:42:11 2021

@author: Gaston
"""
import pandas as pd

'''Ejercicio 8.7
Imprimí las diez especies más frecuentes 
con sus respectivas cantidades.
'''
#Cargo el csv
df_lineal = pd.read_csv('../Data/arbolado-publico-lineal-2017-2018.csv', encoding = 'latin-1')
#Defino las columnas a elegir
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
#Recupero los indices de las diez especies mas frecuentes
especies_frecuentes = df_lineal['nombre_cientifico'].value_counts().head(10).index

print(df_lineal.loc[df_lineal['nombre_cientifico'].isin(especies_frecuentes),cols_sel])
