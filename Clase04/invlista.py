# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 02:14:56 2021

@author: Gaston
"""

'''
Ejercicio 4.5
'''
def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
         invertida.insert(0,e)#agrego el elemento e al principio de la lista invertida
    return invertida

#%%
lista1 = [1, 2, 3, 4, 5]
lista2 = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']

print( invertir_lista(lista1))
print( invertir_lista(lista2))