precios = {}  # Empezamos con un diccionario vacío

with open('../Data/precios.csv', 'rt' , encoding='utf-8') as f:
    for line in f:
        row = line.strip('\n').split(',')
        print(row)
        # precios[ row[0] ] = float( row[1] )
