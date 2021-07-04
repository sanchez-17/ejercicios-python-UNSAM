# -*- coding: utf-8 -*-
"""
Created on Wed May 19 02:33:32 2021

@author: Gaston
"""


class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()

class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()
        
class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))
        
class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''
    def encabezado(self, headers):
        print(f'<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print(f'</tr>', end='')
        print()

    def fila(self, data_fila):
        print(f'<tr>', end='')
        for d in data_fila:
            print(f'<td>{d}</td>', end='')
        print(f'</tr>', end='')
        print()
        
def crear_formateador(nombre):
    if nombre == 'txt':
        formateador = FormatoTablaTXT()
    elif nombre == 'csv':
        formateador = FormatoTablaCSV()
    elif nombre == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format "{nombre}"')
    return formateador

#%%
# def imprimir_tabla(camion, columnas, formateador):
#     formateador.encabezado(columnas)

#     for c in camion:
#         rowdata = [ getattr(c, colname) for colname in columnas ]
#         formateador.fila(rowdata)
