def traductor_geringoso(cadena):
	vowels = 'aeoiu'
	aux = ''

	cadena.lower()

	for c in cadena:

		if c in vowels:            #En caso de ser vocal se añade una silaba con 'p' y c
			
			aux += c + 'p' + c 

		else:					   

			aux += c

	return aux


def dic_geringoso(lista):
	a = []

	for i in lista:
		i = ( i , traductor_geringoso(i))		
		a.append(i)
		
	print( dict(a) )

lista = ['hola','todos']

dic_geringoso(lista)