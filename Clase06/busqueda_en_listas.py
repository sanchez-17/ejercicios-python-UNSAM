# -*- coding: utf-8 -*-
"""
Created on Tue May  4 01:07:57 2021

@author: Gaston
"""

def busqueda_con_index(lista, e):
    '''Busca un elemento e en la lista.

    Si e está en lista devuelve el índice,
    de lo contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

def busqueda_lineal_lordenada(lista,e):
    '''
    Devuelve la posicion de e en lista ordenada, si no está devuelve -1 

    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
        if z > e:
            break    #si z es mayor al elemento buscado detiene la busqueda
    return pos

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    Devuelve numero de comparaciones realizadas (m)
    '''
    if verbose:
        print(f'[DEBUG] izq |medio |der')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    m = 0    #contador de comparaciones
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        m += 1
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{medio:>3d} |{der:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos, m