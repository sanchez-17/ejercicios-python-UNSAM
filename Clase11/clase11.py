# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 00:05:16 2021

@author: Gaston
"""

'''
Ejercicio 11.2: Números triangulares

Escribí una función que calcule recursivamente el n-ésimo número triangular 
(es decir, el número 1 + 2 + 3 + ... + n).
'''

def numero_triangular(n, suma = 0):
    res = suma
    if n != 0:
        res = numero_triangular(n-1, res + n)
    return res

#%%
'''
Ejercicio 11.3: Dígitos

Escribí una función recursiva que reciba un número positivo, n, 
y devuelva la cantidad de dígitos que tiene.
'''

def cantidad_digitos(n):
    '''
    condicion : n >= 0
    devuelve la cantidad de digitos de n
    '''
    if n < 10:
        res = 1
    else:
        res = 1 + cantidad_digitos(n//10)
    return res

#%%
    
'''
Ejercicio 11.4: Potencias

Escribí una función recursiva que reciba 2 enteros, n y b, 
y devuelva True si n es potencia de b.
'''

def es_potencia(n,b):
    '''

    Parameters
    ----------
    n y b enteros

    Returns
    -------
    Si n es potencia de b, retorna True. Sino False.

    '''
    
    if n == 1 or n == b:
        return True
    if b == 1 and n != 1:
        return False
    
    def es_potencia_aux(n, b):
        res = n / b
        if res > b:
            res = es_potencia_aux(res, b)
        return res
    
    try: 
        res = es_potencia_aux(n, b)
        if res == b:
            return True
        else:
            return False
        
    except ZeroDivisionError: #El caso del tipo es_potencia(n,0) ya que n/b = n/0
        return False

#%%
        
'''
Ejercicio 11.5: Subcadenas

Escribí una funcion recursiva que reciba como parámetros dos cadenas a y b,
 y devuelva una lista con las posiciones en donde se encuentra b 
dentro de a.
'''
def posiciones_de(cadena, cadena2, aux = 0):
    posic = []
    if not cadena2 in cadena:
        return []
    else: 
        aux += cadena.index(cadena2)
        posic = [aux] + posiciones_de(cadena[cadena.index(cadena2)+len(cadena2):], cadena2, aux+len(cadena2))
        return posic

#%%

'''
Ejercicio 11.6: Paridad

Escribí dos funciones mutualmente recursivas par(n) e impar(n) 
que determinen la paridad del numero natural dado, usando solo que:

* 1 es impar.
* Un número mayor que uno es impar (resp. par) si su antecesor 
es par (resp. impar).
'''

def impar(n):
    
    def par(n):
        if n == 1:
            res = False
        else:
            res = not par(n-1)
        return res
    
    if n == 1:
        res = True
        
    else:
        if par(n-1):
            res = True
        else:
            res = False
    return res

#%%
    
'''
Ejercicio 11.7: Máximo

Escribí una funcion recursiva que encuentre el mayor elemento de una lista
 (sin usar max()).
'''

def maximo(lista):
    if len(lista)==1:
        res = lista[0]
    else:
        primero = lista[0]
        max_resto = maximo(lista[1:])
        if primero > max_resto:
            res = primero
        else:
            res = max_resto
    return res

#%%
    
'''
Ejercicio 11.8: Replicar

Escribí una función recursiva para replicar los elementos de una lista 
una cantidad n de veces. 
'''

def replicar(lista, n, b = False):
    if not b:
        b = []
        
    cont = n
    if len(lista) == 0:
        return b
    else:
        while cont>0:
            b.append(lista[0])
            cont -= 1
        replicar(lista[1:], n, b)
        return b  

#%%
        
'''
Ejercicio 11.10: Combinatorios

Escribí una función recursiva que reciba una lista de caracteres únicos,
 y un número k, e imprima todas las posibles cadenas de longitud k 
 formadas con los caracteres dados (permitiendo caracteres repetidos).
'''

def combinaciones(lista, n):
    if n == 1:
        return lista
    return [e + c for e in lista \
                  for c in combinaciones(lista, n - 1)]





