# -*- coding: utf-8 -*-
"""
Created on Sun May  9 22:58:00 2021

@author: Gaston
"""

import datetime

'''
Ejercicio 8.1

Escribí una función a la que le pasás tu fecha de nacimiento como 
cadena en formato 'dd/mm/AAAA' (día, mes, año con 2, 2 y 4 dígitos, separados 
con barras normales) y te devuelve la cantidad de segundos que viviste 
(asumiendo que naciste a las 00:00hs de tu fecha de nacimiento).
'''

fecha_nacimiento = '26/12/1996'
object_fecha = datetime.datetime.strptime(fecha_nacimiento, '%d/%m/%Y')

print(f'Segundos vividos desde {object_fecha.date()}: \n{object_fecha.timestamp()} segundos' )

#%%

'''
Ejercicio 8.2

Anunciar la cant de dias faltantes para la primavera
'''

dia_primavera = datetime.date(2021, 9, 22)
dias_restantes = dia_primavera - datetime.date.today()

print(dias_restantes)

#%%

'''
Ejercicio 8.3

Si tenés una licencia por xaternidad que empieza el 26 de septiembre 
de 2020 y dura 200 días, ¿qué día te reincorporás al trabajo?
'''

fecha_licencia = datetime.date(2020,9,26)
fecha_reincorpora = fecha_licencia + datetime.timedelta(days = 200)
print(fecha_reincorpora)

#%%
'''
Ejercicio 8.4
Escribí una función dias_habiles(inicio, fin, feriados) que calcule 
los días hábiles entre dos fechas dadas. La función debe tener como 
argumentos el día inicial, el día final, y una lista con las fechas 
correspondientes a los feriados que haya en ese lapso, y debe devolver 
una lista con las fechas de días hábiles del período, incluyendo la 
fecha inicial y la fecha final indicadas. Las fechas de entrada y 
salida deben manejarse en formato de texto.
'''
def dias_habiles(inicio, fin, feriados):
    
    
    feriados = [datetime.datetime.strptime(feriado, '%d/%m/%Y') for feriado in feriados]
    
    lista = []
    fecha_inicio = datetime.datetime.strptime(inicio, '%d/%m/%Y')
    fecha_fin = datetime.datetime.strptime(fin, '%d/%m/%Y')
    
    fecha = fecha_inicio
    un_dia = datetime.timedelta(days = 1)
    
    while fecha != (fecha_fin + un_dia):
        
        if ( fecha.weekday() not in (5,6) ) and (fecha not in feriados): ##No es sabado, domingo ni feriado
            lista.append(fecha)
        fecha += un_dia
    
    return lista

#%%
    
feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']
dias_habiles_lista = dias_habiles('10/10/2020', '31/12/2020', feriados)
