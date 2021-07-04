# -*- coding: utf-8 -*-
"""
Created on Wed May 19 01:08:38 2021

@author: Gaston
"""

class Lote:
    
    def __init__(self,nombre, cajones,precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    
    def costo(self):
        return self.cajones * self.precio
    
    def vender(self, cant):
        self.cajones -= cant
        
    def __repr__(self):
        return f"Lote('{self.nombre}',{self.cajones},{self.precio})"
#%%
        
'''Ejercicio 9.3'''
# import fileparse

# with open('../Data/camion.csv') as lineas:
#     camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
# ...
# camion = [ Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]

# camion
# sum([c.costo() for c in camion])
