# -*- coding: utf-8 -*-
'''Ordenamiento por selección'''
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
'''Ordenamiento por inserción'''

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
Ejercicio 12.5: comparar métodos gráficamente
'''
from burbujeo import ord_burbujeo

def generar_lista(N):
    import numpy as np
    lista = np.random.randint(1,1000,N)
    return list(lista)
#%%
N = 256
comparaciones_burbujeo = []
comparaciones_seleccion = []
comparaciones_insercion = []

for i in range(1,N+1):
    lista = generar_lista(i)
    comparaciones_burbujeo.append( ord_burbujeo(lista.copy()) )
    comparaciones_seleccion.append( ord_seleccion(lista.copy()) )
    comparaciones_insercion.append( ord_insercion(lista.copy()) )

#%%

import matplotlib.pyplot as plt

plt.plot(comparaciones_burbujeo, label= 'Bubble sort')
plt.plot(comparaciones_seleccion, label = 'Selection sort')
plt.plot(comparaciones_insercion, label = 'Insertion sort', linestyle = 'dashed')
plt.title('Comparación de algoritmos de ordenamiento')
plt.legend()
plt.show()

#%%

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    comp = 0
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        comp += izq[1] + der[1]
        lista_nueva, comp= merge(izq[0], der[0], comps = comp)
        
    return lista_nueva, comp

def merge(lista1, lista2, comps = 0):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        comps += 1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, comps
#%%
'''
Ejercicio 12.7
'''
N = 256
comparaciones_burbujeo = []
comparaciones_seleccion = []
comparaciones_insercion = []
comparaciones_merge = []

for i in range(1,N+1):
    lista = generar_lista(i)
    comparaciones_burbujeo.append( ord_burbujeo(lista.copy()) )
    comparaciones_seleccion.append( ord_seleccion(lista.copy()) )
    comparaciones_insercion.append( ord_insercion(lista.copy()) )
    comparaciones_merge.append( merge_sort(lista.copy())[1] )
    
import matplotlib.pyplot as plt

plt.plot(comparaciones_burbujeo, label= 'Bubble sort')
plt.plot(comparaciones_seleccion, label = 'Selection sort')
plt.plot(comparaciones_insercion, label = 'Insertion sort', linestyle = 'dashed')
plt.plot(comparaciones_merge, label = 'Merge sort')
plt.title('Comparación de algoritmos de ordenamiento')
plt.legend()
plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    