import informe

def costo_camion(nombre_archivo):
    suma = 0
    rows = informe.leer_camion(nombre_archivo)
    for n_row, row in enumerate(rows):
        try:
            suma += row.cajones * row.precio
        # Esto atrapa errores en los int() y float() de arriba.
        except ValueError:
            print(f'Fila {n_row}: No pude interpretar: {row}')
    print(suma)

costo_camion('../Data/camion.csv')

# informe.informe_camion('../Data/camion.csv', '../Data/precios.csv')