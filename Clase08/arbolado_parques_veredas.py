# -*- coding: utf-8 -*-
"""
Created on Wed May 12 02:05:14 2021

@author: Gaston
"""

import pandas as pd
import seaborn as sns

#Cargamos los csv
df_parques = pd.read_csv('../Data/arbolado-en-espacios-verdes.csv')
df_veredas = pd.read_csv('../Data/arbolado-publico-lineal-2017-2018.csv')

cols_sel_veredas = ['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']
cols_sel_parques = ['nombre_cie', 'diametro', 'altura_tot']

#Seleccionamos las filas de 'Tipuana Tipu' con sus respectivas columnas
df_tipas_parques = df_parques.loc[df_parques['nombre_cie'] == 'Tipuana Tipu',cols_sel_parques].copy()
df_tipas_veredas = df_veredas.loc[df_veredas['nombre_cientifico'] == 'Tipuana tipu',cols_sel_veredas].copy()

#Renombramos columnas y agregamos segun ambiente
df_tipas_parques.rename(columns={"nombre_cie": "nombre_cientifico", "diametro": "diametro_altura_pecho" , "altura_tot" : "altura_arbol"}, inplace = True)
df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'

#mergeamos
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

#Ploteamos
df_tipas.boxplot('diametro_altura_pecho', by = 'ambiente')
df_tipas.boxplot('altura_arbol', by = 'ambiente')