import csv

def leer_precios(nombre_archivo):
	precios = {}
	f = open(nombre_archivo, 'rt', encoding = 'utf-8')
	rows = csv.reader(f)
	headers = next(rows)
	try:
		for row in rows:
			precios[row[0]] = float( row[1])

	except:
		pass

	return precios
