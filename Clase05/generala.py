# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 12:54:59 2021

@author: Gaston
"""


'''
Ejercicio 5.1
'''

import random

def tirar(n):
    tirada = [random.randint(1,6) for i in range(n)]
    return tirada

def es_generala(tirada):
    res = True
    primer_numero = tirada[0]
    for i in tirada:
        if primer_numero != i : 
            res = False
            break
    return res

N=100000
G = sum([es_generala(tirar(5)) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
#%%
# def es_generala(tirada):
#     return max(tirada) == min(tirada)
from matplotlib import pyplot as plt

N=1000000
sumas= [sum( tirar(5) ) for i in range(N) ]

plt.hist(sumas, bins=25 )# , density=True)
#%%

'''
Ejercicio 5.2
'''

from collections import Counter
    
def generala():
    
    tirada_1 = tirar(5)
    mas_repetido = Counter(tirada_1).most_common()[0][0]
    n_repetido = Counter(tirada_1).most_common()[0][1]
    k = 0
    while k < n_repetido:

        for i in tirada_1:
            if i != mas_repetido:
                tirada_1.remove(i)
        k += 1
    '''Segunda tirada'''
    tirada_2 = tirar((5-len(tirada_1)))
    if len(tirada_2) != 0:
        n_repetido_2 = Counter(tirada_2).most_common()[0][1]

        if  n_repetido_2 > n_repetido : 
            mas_repetido = Counter(tirada_2).most_common()[0][0]
            tirada_1 = [mas_repetido]*n_repetido_2 
        else:
            for i in tirada_2:
                if i in tirada_1:
                    tirada_1.append(i)

    '''Tercera tirada'''
    tirada_3 = tirar((5-len(tirada_1)))

    if len(tirada_3) != 0:
        n_repetido_3 = Counter(tirada_3).most_common()[0][1]

        if  n_repetido_3 > n_repetido and n_repetido_3 > n_repetido_2  : 
            mas_repetido = Counter(tirada_3).most_common()[0][0]
            tirada_1 = [mas_repetido]*n_repetido_3
        else:
            for i in tirada_3:
                if i in tirada_1:
                    tirada_1.append(i)

    return tirada_1

a = generala()
N = 10000000
G = sum([len(generala())==5 for i in range(N)])
prob = G/N
print(f'Jugué {N} manos, de las cuales {G} saqué generala.')
print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')