cadena = 'geringoso'
vowels = 'aeoiu'
aux = ''

cadena.lower()

for c in cadena:

	if c in vocals:            #En caso de ser vocal se añade una silaba con 'p' y c
		
		aux += c + 'p' + c 

	else:					   

		aux += c
		
print(aux)