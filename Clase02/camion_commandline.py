# camion_commandline.py
import csv
import sys
def costo_camion(nombre_archivo):
	suma = 0
	with open(nombre_archivo, 'rt', encoding = 'utf-8') as f:
		next(f)
		for line in f:
			a = line.split(',')
			suma += int( a[1] ) * float( a[2] )

		return suma

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)