# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:24:17 2021

@author: Gaston
"""

import csv

def parse_csv(file, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas,
    determinando el parámetro select, que debe ser una lista de nombres
    de las columnas a considerar.
    '''
    rows = csv.reader(file)
    n_line = 0
    
    if has_headers:
        headers = next(rows)
        n_line = 1
    
    #si se habilita seleccion de columnas
    if select and has_headers:
        indices = [ headers.index(columna) for columna in select]
    else:
        indices = []
    
    
    #En caso de elegir columnas y no tenga encabezados, levanta error
    if select and not has_headers:
        raise RuntimeError("Para seleccionar, necesito encabezados.")
            
    
    registros = []
    
    
    for n_row, row in enumerate(rows,start=n_line):
        if not row:
            continue
        if indices:
            row = [row[index] for index in indices]
        
        #si se habilita parseo de columnas
        if types:
            try:
                row = [func(val) for func, val in zip(types, row) ]
            except ValueError as e:
                if silence_errors is not True:
                    print(f'Fila {n_row}: No pude convertir: {row}')
                    print(f'Fila {n_row}: Motivo: {e}')
                continue
        #Si el archivo no tiene encabezados
        if not has_headers:
            registros.append(tuple(row))
        else:
            registro = dict(zip(headers,row))
            registros.append(registro)
            
    return registros