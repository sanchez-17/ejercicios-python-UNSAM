# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 16:52:09 2021

@author: Gaston
"""

def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
         invertida.insert(0,e)#agrego el elemento e al principio de la lista invertida
    return invertida


def propagar(lista1):
    '''
    Parameters
    ----------
    lista : reciba un vector 
    con 0's, 1's y -1's y devuelva un vector 
    el que los 1's se propagaron a sus vecinos con 0. 
    '''
    lista = list(lista1)
    for i, e in enumerate(lista):
        try :
            if (e == 0 and lista[i+1] == 1) or ( e==0 and lista[i-1] == 1 ):
                lista[i] = 1
            if e == 1 and lista[i+1] == 0  :
                lista[i+1] = 1
            if e == 1 and i>0 and lista[i-1] == 0  :
                lista[i-1] =1
        except IndexError:
            continue
    
    lista = invertir_lista(lista)

    '''
    recorro la lista en sentido inverso
    '''
    for i,e in enumerate(lista):
        try :
            if (e == 0 and lista[i+1] == 1) or ( e==0 and lista[i-1] == 1):
                lista[i] = 1
            if e == 1 and lista[i+1] == 0  :
                lista[i+1] = 1
            if e == 1 and i<0 and lista[i-1] == 0  :
                lista[i-1] =1
        except IndexError:
            continue
    
    lista = invertir_lista(lista)
    
    return lista

# lista = [ 0, 0, 0, 1, 0, 0]
# res1 = [ 1, 1, 1, 1, 1, 1]

lista_a_probar = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
respuesta_esperada = [0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1]

respuesta = propagar(lista_a_probar)

print(respuesta == respuesta_esperada)
