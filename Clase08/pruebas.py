# -*- coding: utf-8 -*-
"""
Created on Mon May 10 01:42:02 2021

@author: Gaston
"""

import datetime

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
