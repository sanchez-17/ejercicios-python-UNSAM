# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 02:00:14 2021

@author: Gaston
"""


'''
Ejercicio 4.3
'''

def buscar_u_elemento(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in reversed(list(enumerate(lista))): # recorremos la lista desde el final
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

res = buscar_u_elemento([1,2,3,2,3,4],5)
print(res)

def buscar_n_elemento(lista, e):
    '''Devuelve la cantidad de veces que aparece e'''
    cont = 0
    for i in lista:
        if e == i:
            cont += 1
    return cont

#%%
res = buscar_n_elemento([1,2,3,2,3,4],1)
print(res)

#%%
'''
Ejercicio 4.4
'''

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = 0 # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m

res = maximo([1,2,3,2,-1])
print(res)

