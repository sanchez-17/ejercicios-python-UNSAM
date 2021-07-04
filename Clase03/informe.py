import csv
from pprint import pprint

def leer_camion(nombre_archivo):
	camion = [] 					#Se crea la lista para los datos del camion
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
	#Imprimo resultados y devuelvo el balance
	# print('Frutas sin precio y sin vender:',lista_frutas_sin_precio)
	# print(f'Costo del camion: ${costo_camion:0.2f}')
	# print(f'Recaudación de la venta: ${costo_venta}')
	return costo_venta - costo_camion

def leer_precios(nombre_archivo):
	#Crea un diccionario para almacenar los precios por fruta
	precios = {}
	#Lee los archivos y saltea el encabezado
	f = open(nombre_archivo, 'rt', encoding = 'utf-8')
	rows = csv.reader(f)
	headers = next(rows)
	#lee cada fruta y la agrega al diccionario 'precios'
	try:
		for row in rows:
			precios[row[0]] = float( row[1])

	except:
		pass

	return precios

a = balance('../Data/camion.csv','../Data/precios.csv')
#imprimo resultados
print(f'Balance: ${a:0.2f}')