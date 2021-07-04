# -*- coding: utf-8 -*-
"""

"""
def ord_burbujeo(lista):
    contador_comp = 0
    for i in range(0, len(lista) - 1):
        for j in range(0, len(lista) - 1):
            contador_comp += 1
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return contador_comp
