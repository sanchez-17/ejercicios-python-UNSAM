# -*- coding: utf-8 -*-
"""
Created on Tue May 11 17:51:45 2021

@author: Gaston
"""

import os

def listar_png(directorio):
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if '.png' in name:
                print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))

def main(argv):
    if len(argv) != 2:
        print(f'Uso correcto: \n{argv[0]} DIRECTORIO')
    else:
        directorio = argv[1]
        listar_png(directorio)
        
if __name__ == '__main__':
    import sys
    main(sys.argv)
    
# directorio = '../Data/ordenar'
# listar_png(directorio)
