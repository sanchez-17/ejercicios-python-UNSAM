# -*- coding: utf-8 -*-
"""
Created on Tue May  4 20:43:45 2021

@author: Gaston
"""
# import numpy as np

def incrementar(s):
    carry = 1
    l = len(s)
    
    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s

def listar_secuencias(n):
    '''
    Devuelva una lista con todas las secuencias binarias de longitud n 
    comenzando con la primera ([0]*n)
    Complejidad : O(2**n)
    '''
    lista = []
    a = [0]*n
    lista.append(a.copy())
    control = True                     #variable de control
    
    while control is not False:
        a = incrementar(a)
        
        if sum(a) == 0:
            control = False
            continue
        
        lista.append(a.copy())
        
    return lista
    
lista = listar_secuencias(6)