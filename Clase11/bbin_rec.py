# -*- coding: utf-8 -*-
"""
Ejercicio 11.11: Búsqueda binaria

Escribí una función recursiva que implemente la búsqueda 
binaria de un elemento e en una lista ordenada lista. 
La función debe devolver simplemente True o False indicando si el elemento 
está o no en la lista.
"""

def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if lista[medio] == e:
            res = True
        elif lista[medio] > e:
            res = bbinaria_rec(lista[:medio],e)
        else:
            res = bbinaria_rec(lista[medio+1:],e)
            

    return res
