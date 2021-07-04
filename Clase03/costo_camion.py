import csv

def costo_camion(nombre_archivo):
	suma = 0
	with open(nombre_archivo, 'rt', encoding = 'utf-8') as f :
		lines = csv.reader(f)
		headers = next(lines)
		for n_line, line in enumerate(lines,start=1):
			record = dict(zip(headers, line))
			try:
				ncajones = int(record['cajones'])
				precio = float(record['precio'])
				suma += ncajones * precio
				# Esto atrapa errores en los int() y float() de arriba.
			except ValueError:
				print(f'Fila {n_line}: No pude interpretar: {line}')

	print('Costo total',suma)
