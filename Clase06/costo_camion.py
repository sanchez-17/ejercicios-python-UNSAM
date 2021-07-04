from informe_funciones import leer_camion

def costo_camion(nombre_archivo):
    suma = 0
    rows = leer_camion(nombre_archivo)
    for n_row, row in enumerate(rows,start=1):
        try:
            suma += row['cajones'] * row['precio']
        # Esto atrapa errores en los int() y float() de arriba.
        except ValueError:
            print(f'Fila {n_row}: No pude interpretar: {row}')
    print('Costo total:',suma)

costo_camion('../Data/camion.csv')