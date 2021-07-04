# -*- coding: utf-8 -*-
"""
Created on Wed May  5 12:43:07 2021

@author: Gaston
"""

def valor_absoluto(n):
    '''Calcula el valor absoluto de n

    Pre: n tiene que ser un numero entero
    Pos: Se devuelve el valor absoluto de n
    
    '''
    if n >= 0:
        return n
    else:
        return -n

#Invariante: si n es positivo n conserva su valor, sino se multiplica por -1
#%%
def suma_pares(l):
    '''Calcula la suma de los numeros pares de una lista

    Pre: los elementos de l enteros
    Pos: Se devuelve la suma de sus enteros pares
    
    '''
    res = 0
    for e in l:
        
        if e % 2 ==0:
            res += e
        else:
            res += 0
    return res

#invariante: res conserva su valor hasta que se encuentre un numero par en lista
#%%
def veces(a, b):
    '''Suma b veces el numero a

    Pre: a numeros entero, b numero entero positivo
    Pos: Se devuelve el resultado de a * b
    
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

#invariante: El valor de b decrece en cada ciclo hasta cero
#            res se acerca al valor buscado
#            res = a * (b - nb)
#%%
def collatz(n):
    '''Devuelve el numero de veces que se pueda aplicar la funcion de collatz
    hasta obtener un 1.

    Pre: n > 0
    Pos: numeros de veces que se aplicó la función
    
    '''
    res = 1

    while n != 1:
        if n % 2 == 0:       # si n es par, se divide entre 2.
            n = n//2
        else:               #Si n es impar, se multiplica por 3 y se suma 1.
            n = 3 * n + 1
        res += 1

    return res
