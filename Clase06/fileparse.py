# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:24:17 2021

@author: Gaston
"""

import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas,
    determinando el parámetro select, que debe ser una lista de nombres
    de las columnas a considerar.
    '''
    with open(nombre_archivo, 'rt',encoding = 'utf-8') as f:
        rows = csv.reader(f)
        
        if has_headers:
            headers = next(rows)
        
        if select and has_headers:
            indices = [ headers.index(columna) for columna in select]
        else:
            indices = []
        
        registros = []
        
        for row in rows:
            if not row:
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row) ]
                
            if not has_headers:
                registros.append(tuple(row))
            else:
                registro = dict(zip(headers,row))
                registros.append(registro)
            
    return registros