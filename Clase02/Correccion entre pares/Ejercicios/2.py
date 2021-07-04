import csv

def costo_camion(lista_camion):
    costo_total = 0

    for item in lista_camion:
        costo_total += item['cajones'] * item['precio']

    return costo_total

# Ejercicio 2.15: Lista de tuplas

# def leer_camion(nombre_archivo):

#     with open(nombre_archivo, 'rt') as file:
#         rows = csv.reader(file)
#         headers = next(rows)
#         camion = []

#         for row in rows:
#             tupla = (row[0], int(row[1]), float(row[2]))
#             camion.append(tupla)

#         return camion

# Ejercicio 2.16: Lista de diccionarios

def leer_camion(nombre_archivo):

    camion = []

    with open(nombre_archivo, 'rt', encoding='utf-8') as file:
        rows = csv.reader(file)
        headers = next(rows)

        for row in rows:
            diccionario = {}
            diccionario[headers[0]] = row[0]
            diccionario[headers[1]] = int(row[1])
            diccionario[headers[2]] = float(row[2])

            camion.append(diccionario)

    return camion


# Ejercicio 2.17: Diccionarios como contenedores
def leer_precios(nombre_archivo):
    diccionario = {}

    with open(nombre_archivo, 'rt', encoding='utf-8') as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                diccionario[row[0]] = float(row[1])
            except IndexError:
                pass

    return diccionario


def costo_venta(precios_camion, precios_venta):
    costo = 0

    for item in precios_camion:
        fruta = item['nombre']
        costo += item['cajones'] * precios_venta[fruta]
    
    return costo


def balance(nombre_archivo):
    precios_camion = leer_camion(nombre_archivo)
    recaudacion_camion = costo_camion(precios_camion)

    precios_venta = leer_precios('../Data/precios.csv')
    recaudacion_venta = costo_venta(precios_camion, precios_venta)

    diferencia = recaudacion_venta - recaudacion_camion

    if diferencia > 0:
        estado = "Ganancia"
    else:
        estado = "Pérdida"
        diferencia = diferencia * -1

    return f"""
Costo camion: {recaudacion_camion}
Recaudacion venta: {recaudacion_venta}
{estado}: {round(diferencia,2)}
"""

# costo = costo_camion('Data/camion.csv')
# print('Costo total:', costo)

# data_camion = leer_camion('Data/camion.csv')
# print(data_camion)

# precios = leer_precios('Data/precios.csv')
# print(precios['Rúcula'])

print(balance('../Data/camion.csv')) # Costo camion: 47671.15
                                  # Recaudacion venta: 62986.1
                                  # Ganancia: 15314.95"""