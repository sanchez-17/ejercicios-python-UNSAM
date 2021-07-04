def costo_camion(nombre_archivo):
	suma = 0
	with open(nombre_archivo, 'rt', encoding = 'utf-8') as f :
		headers = next(f)
		for line in f:
			a = line.split(',')
			suma += int( a[1] ) * float( a[2]) 

	print('Costo total',suma)


