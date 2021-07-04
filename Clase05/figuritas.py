# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 20:31:47 2021

@author: Gaston
"""


import random
import numpy as np

def crear_album(figus_total):
    '''Crea array nulo de longitud figus_total'''
    return np.zeros(figus_total, dtype=np.int64)

def album_incompleto(A):
    '''Devuelve True si el array A tiene al menos un cero'''
    return sum( A == 0) != 0

def comprar_figu(figus_total):
    '''Devuelve un numero entero de 1 a figus_total'''
    return random.randint(1,figus_total)

def cuantas_figus(figus_total):
    '''Devuelve el numero de figus totales compradas 
    hasta completar el album'''
    
    album = crear_album(figus_total)
    while album_incompleto(album):# mientras el album esté incompleto
        album[ comprar_figu(figus_total) - 1 ] += 1 #Compra una figu y la pega en el album
    return sum(album)

# n_repeticiones = 100
# figus_total = 670

#Lista que registra cuantas figus fueron compradas hasta completar el album en cada iteración 
# lista = [cuantas_figus(figus_total) for i in range(n_repeticiones) ]
# print( np.mean(lista))

#%%
'''Ejercicio 5.16'''

def comprar_paquete(figus_total, figus_paquete):
    '''Devuelve un paquete de figus del tamaño de "figus_paquete" '''
    return [ random.randint(1,figus_total) for i in range(figus_paquete)]

#%%
    
'''Ejercicio 5.17'''

def cuantos_paquetes(figus_total, figus_paquete):
    '''Compra el album vacio y un paquete'''
    album = crear_album(figus_total)
    paquete = comprar_paquete(figus_total, figus_paquete)

    while album_incompleto(album):
        '''Pega cada figu del paquete en el album'''
        for figu in paquete:
            album[ figu - 1 ] += 1
        '''compra un paquete nuevo '''
        paquete = comprar_paquete(figus_total, figus_paquete)
        
    return sum(album) / figus_paquete

#%%
'''Ejercicio 5.18'''

n_repeticiones = 100
figus_total = 670
figus_paquete = 5

lista = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones) ]
lista = np.array(lista, dtype = np.int64)
print( np.mean(lista))

#%%


import matplotlib.pyplot as plt

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop() - 1] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()


#%%
'''Ejercicio 5.19'''

lista = np.array(lista)
probabilidad = (lista <= 850).sum() / len(lista)

#%%

'''Ejercicio 5.20'''

plt.hist(lista,bins=20, density=True)
plt.xlabel("Cantidad de paquetes")
plt.ylabel("Probabilidad")
plt.title("Cantidad de paquetes comprados hasta llenar el album")
plt.show()

#%%

'''Ejercicio 5.21'''

def sacar_probabilidad(lista, proba):
    a = []
    for i in range( max(lista) ):
        res = (lista <= i).sum() / len(lista)
        if res == proba:
            a.append(i)
    return int(np.mean(a))

proba = 0.9
cant_de_paq = sacar_probabilidad(lista, proba)
print( f"Cantidad de paquetes con { proba * 100 : .0f} % de probabilidad de llenar el album: {cant_de_paq}" )
        
#%%
#otra forma
probabilidad = 90
cant_de_paq = np.percentile(lista, proba)
print( f"Cantidad de paquetes con { proba * 100 : .0f} % de probabilidad de llenar el album: {cant_de_paq}" )
#%%

'''Ejercicio 5.22'''

def comprar_paquete_sin_repe(figus_total, figus_paquete):
    '''Devuelve un paquete de figus del tamaño de "figus_paquete" sin figus repetidas'''
    return random.sample( range(1,figus_total + 1) , k = figus_paquete)

def cuantos_paquetes_sin_repe(figus_total, figus_paquete):
    '''Compra el album vacio y un paquete'''
    album = crear_album(figus_total)
    paquete = comprar_paquete_sin_repe(figus_total, figus_paquete)

    while album_incompleto(album):
        '''Pega cada figu del paquete en el album'''
        for figu in paquete:
            album[ figu - 1 ] += 1
        '''compra un paquete nuevo'''
        paquete = comprar_paquete_sin_repe(figus_total, figus_paquete)
        
    return sum(album) / figus_paquete

n_repeticiones = 100
figus_total = 670
figus_paquete = 5

lista = [cuantos_paquetes_sin_repe(figus_total, figus_paquete) for i in range(n_repeticiones) ]
lista = np.array(lista, dtype=np.int64)
