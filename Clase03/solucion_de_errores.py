#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era del tipo semántico y estaba ubicado en el bucle while.
#    Solo verificaba si tenía 'a' en el primer carácter de la cadena
#    No contemplaba los casos con mayúsculas o tildes
#    Lo corregí cambiando el argumento del if, el modo en que retorna el valor y añadiendo el metodo 'lower'
def tiene_a(expresion):
	expresion = expresion.lower()
	n = len(expresion)
	i = 0
	while i<n:
		if expresion[i] in 'aá':
			return True
		i += 1
	return False

rta = tiene_a ('palabra')
print(rta)
#%%
tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.2. Función tiene_a()
#Comentario: El error era del tipo sintáctico y estaba ubicado en el bucle while.
#    No contemplaba los casos con mayúsculas o tildes
#    Lo corregí cambiando el argumento del if y añadiendo el metodo 'lower'
#	 Los errores de sintaxis estaban en el argumento del if, cuando retornaba False y 
#    los 'dos puntos' faltantes.

def tiene_a(expresion):
    expresion = expresion.lower()
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'aá':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: Falla al ejecutar la funcion con un parámetro del tipo int.
#   Lo arregle parseando la variable 'expresion' al tipo string al comienzo 
#   de la función.


def tiene_uno(expresion):
	expresion = str(expresion)
	n = len(expresion)
	i = 0
	tiene = False
	while (i<n) and not tiene:
		if expresion[i] == '1':
			tiene = True
		i += 1
	return tiene

#%%
#Ejercicio 3.4. Función suma()
#Comentario: No devuelve ninguna respuesta.
#   Lo arregle retornando el valor de c

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.5. Función leer_camion()
#Comentario: Todas las entradas tenian el mismo valor.
#   Lo arregle reiniciando el diccionario registro en cada iteración.

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
        	registro[encabezado[0]] = fila[0]
        	registro[encabezado[1]] = int(fila[1])
        	registro[encabezado[2]] = float(fila[2])
        	camion.append(registro)
        	registro = {}
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)