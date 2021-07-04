import informe

def costo_camion(nombre_archivo):
    '''
    Computa el precio total (cantidad * precio) de un archivo camion
    '''
    camion = informe.leer_camion(nombre_archivo)
    return camion.precio_total()

# print(costo_camion('../Data/camion.csv'))

