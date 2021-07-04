def buscar_precio(fruta):
	control = True
	try:
		with open('../Data/precios.csv', 'rt', encoding = 'utf-8') as f:
			
			for line in f:
				info = line.split(',')
				if info[0] == fruta :
					print('El precio de la', fruta , 'es:', info[1])
					control = False
			if control == True:
				raise	
	except: 			
		print('No se ha encontrado el resultado, intente nuevamente ')


