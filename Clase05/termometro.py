# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 13:52:52 2021

@author: Gaston
"""

import random
import numpy as np

n = 999
media = 37.5

term = [ random.normalvariate( media, 0.2) for i in range(99)]
term = np.array(term)

np.save('../Data/Temperaturas.npy', term)

print(f'|Mínimo: {min(term)}\n\
|Máximo: {max(term)}\n\
|Promedio: {sum(term) / len(term) }\n\
|Mediana: {sorted(term)[int(len(term)/2)]}')

