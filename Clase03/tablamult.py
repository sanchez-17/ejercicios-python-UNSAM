# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 13:43:35 2021

@author: Gaston
"""
def tabla(n):
    print('      ', end='')
    for i in range(n):
        print(f'{i:>5}', end='')
    print('\n      ',end="")
    print('-----'*n, end="\n")
    for x in range(n):
        valor = 0
        print(f"{x:>5}|", end= "")
        for y in range(n):
            print(f"{valor:>5}", end= "")
            valor += x
        print("")

tabla(5)