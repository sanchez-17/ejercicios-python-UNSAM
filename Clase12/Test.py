# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 22:14:32 2021

@author: Gaston
"""
import random

def ord_burbujeo(lista):
    
    for i in range(0, len(lista) - 1):
        for j in range(0, len(lista) - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
            
    return lista

def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    return l


def experimento_comps_bur(k):
    comps_tot_bur = 0
    for i in range(k):
        comps_tot_bur += ord_burbujeo(lista.copy())[1]
    return comps_tot_bur/k


k = 10
m = 1000
n = 256
lista = generar_lista(n, m)
print (experimento_comps_bur(k))
#%%

esto me genera el siguiente resultado, esto seria para una sola lista de 256 enteros:
32640.0
Cuando quiero largarlo completo el codigo el siguiente (256 listas con cantidad de enteros entre 1 y 256):
n= 256
m=1000
k= 10
largos = np.arange(n) + 1 # estos son los largos de listas que voy a usar
comps_bur = np.zeros(n)
for i, n in enumerate(largos):
    lista = generar_lista(n, m)
    comps_bur[i] = experimento_comps_bur(k)