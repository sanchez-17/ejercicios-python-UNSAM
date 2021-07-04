# -*- coding: utf-8 -*-
"""

"""

def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    contador_comp = 0
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        contador_comp += n
        p = buscar_max(lista, 0, n)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        #print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1
    return contador_comp

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""
    
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

#%%
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    contador_comp = 0
    
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            contador_comp += i+1
            reubicar(lista, i + 1)
        #print("DEBUG: ", lista)
    return contador_comp

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v
#%%

'''
Ejercicio 12.4: experimento con 3 métodos

Hacé una función generar_lista(N) que genere una lista aleatoria de largo N con números enteros del 1 al 1000 (puede haber repeticiones).
Modificá el código de las tres funciones para que cuenten cuántas comparaciones entre elementos de la lista realiza cada una. Por ejemplo, ord_seleccion realiza comparaciones (entre elementos de la lista) sólo cuando llama a buscar_max(lista, a, b) y en ese caso realiza b-a comparaciones.
Realizá un experimento que genere una lista de largo N y la ordene con los tres métodos (burbujeo, inserción y selección).
Para N = 10, realizá k = 100 repeticiones del siguiente experimento. Generar una lista de largo N, ordenarlas con los tres métodos y guardar la cantidad de operaciones. Al final, debe imprimir el promedio de comparaciones realizado por cada método.
'''

from burbujeo import ord_burbujeo
import numpy as np

def generar_lista(N):
    import numpy as np
    lista = np.random.randint(1,1000,N)
    return list(lista)

N = 10
k = 100
total_comps_burbujeo = []
total_comps_seleccion = []
total_comps_insercion = []

for i in range(k):
    lista = generar_lista(N)
    total_comps_burbujeo.append( ord_burbujeo(lista.copy()) )
    total_comps_seleccion.append( ord_seleccion(lista.copy()) )
    total_comps_insercion.append( ord_insercion(lista.copy()) )

burb = np.mean(total_comps_burbujeo)
sel = np.mean(total_comps_seleccion)
ins = np.mean(total_comps_insercion)

print(f'\nResultados: \nBurbujeo:{burb}\nSelección:{sel}\nInserción:{ins}')















