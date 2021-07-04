# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 12:19:44 2021

@author: Gaston
"""
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
	camion = [] 			#Se crea la lista para los datos del camion
	with open(nombre_archivo, 'rt', encoding = 'utf-8') as f:
		#lee los datos del archivo
		rows = csv.reader(f)		
		headers = next(rows)
		#Por cada lote crea un diccionario y lo agrega a la lista
		for row in rows:
			lote = dict(zip(headers,row))
			#lote = dict( ( ('nombre',row[0]), ('cajones', int(row[1]) ) ,('precio', float(row[2])) ) )
			camion.append(lote)

	return camion #Devuelve la lista

def balance(nombre_camion, nombre_precios):
	#Instancio los valores para los costos y leo los archivos del camion y la lista de precios
	camion = leer_camion(nombre_camion)
	precio = leer_precios(nombre_precios)
	costo_camion = 0
	costo_venta = 0
	#Calcula el costo del camion y estima la venta de los productos existentes en el camion
	for cajon in camion:
		try:
			costo_camion += int( cajon['cajones'] ) * float( cajon['precio'] )
			costo_venta += int( cajon['cajones'] ) * float( precio[ cajon['nombre'] ] )
		except:
			#Si un lote no tiene precio de venta lo agrega a una lista y no se toma en cuenta en la venta
			lista_frutas_sin_precio = []
			lista_frutas_sin_precio.append(cajon['nombre'])
			continue

	return costo_venta - costo_camion

def hacer_informe(camion, precios):

    salida = []
    for i in camion:
        try:
            salida.append( (i['nombre'], int(i['cajones']), float(precios[i['nombre']]) , float(precios[i['nombre']]) - float(i['precio'])))
        except KeyError:
            pass
    return salida

def leer_precios(nombre_archivo):
	#Crea un diccionario para almacenar los precios por fruta
	precios = {}
	#Lee los archivos y saltea el encabezado
	f = open(nombre_archivo, 'rt', encoding = 'utf-8')
	rows = csv.reader(f)
	next(rows)
	#lee cada fruta y la agrega al diccionario 'precios'
	try:
		for row in rows:
			precios[row[0]] = float( row[1])

	except:
		pass

	return precios

def preparar_informe(archivo_camion , archivo_precios):
    
    res = balance(archivo_camion,archivo_precios)
    lista_camion = leer_camion(archivo_camion)
    lista_precios = leer_precios(archivo_precios)
    
    informe = hacer_informe(lista_camion, lista_precios)
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    
    return res, informe, headers

def imprimir_informe(informe):
    headers = informe[2]
    balance = informe[0]
    
    print(f'Balance: ${balance:0.2f}')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'---------- ' * len(headers))
    for nombre, cajones, precio, cambio in informe[1]:
        precio_aux = f'${round(precio,2)}'
        print(f'{nombre:>10s} {cajones:>10d} {precio_aux:>10s} {cambio:>10.2f}')

#imprimo resultados

informe = preparar_informe('../Data/camion.csv', '../Data/precios.csv')
imprimir_informe(informe)
