# -*- coding: utf-8 -*-


def pascal(n, k):
    '''
    Calcula el valor que se encuentra en la fila n y la columna k 
    del triangulo de pascal.
    '''
    if k>n:
        print('Fuera de rango')
        return

    if k == 0 or k == n:   #Caso base: si es el primer elemento o extremo de la fila, vale 1
        return 1
    else:
        res = pascal(n-1,k-1) + pascal(n-1,k)
    return res