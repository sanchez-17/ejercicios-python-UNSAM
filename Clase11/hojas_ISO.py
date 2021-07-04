# -*- coding: utf-8 -*-
"""
Ejercicio 11.13: Hojas ISO y recursión

Escribí una función recursiva que para una entrada N mayor que cero, 
devuelva el ancho y el largo de la hoja A(N) calculada recursivamente a partir
 de las medidas de la hoja A(N−1), usando la hoja A0 como caso base.
"""

def hojasISOA(n):
    if n == 0:  
        res = [841,1189]
    else:
        #El siguiente formato se obtiene doblando la hoja por el lado más grande
        aux = hojasISOA(n-1)
        # Busca el indice del lado mas largo y lo divide por 2
        idx_max = aux.index(max(aux))  
        aux[idx_max] /= 2
        
        res = aux
    return res
        
