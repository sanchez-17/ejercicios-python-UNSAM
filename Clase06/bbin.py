# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:39:12 2021

@author: Gaston
"""


def donde_insertar(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Si x no está en lista, devuelve la posición tal que x en lista[pos], lista sigue ordenada
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |medio |der')
    izq = 0
    der = len(lista) - 1
    
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{medio:>3d} |{der:3d}')
        if lista[medio] == x:
            return medio    #Elemento encontrado
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    pos = medio
    return pos

def insertar(lista, x):
    '''
    Si x se encuentra en lista solamente devuelve su posición
    si no se encuentra en la lista, lo inserta en la posición correcta 
    para mantener el orden y devuelve su posición
    '''
    pos = donde_insertar(lista, x)
    if x == lista[pos]:
        return pos
    else:               # si x != lista[pos]
        lista[pos] = x
        return pos