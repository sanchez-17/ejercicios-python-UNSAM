# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 23:51:11 2021

@author: Gaston
"""


'''
Ejercicio 5.4
'''
import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

n = 100000
M = 0
for i in range(n):
    x, y= generar_punto()
    if x**2 + y**2 < 1 :
        M += 1

print(f'pi ~ {M/n * 4: .5f}')