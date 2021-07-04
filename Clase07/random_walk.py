# -*- coding: utf-8 -*-
"""
Created on Mon May  3 13:08:18 2021

@author: Gaston
"""
import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)
    return pasos.cumsum()

maximos = []
caminatas = []

for i in range(100):
    pasos = randomwalk(12)
    maximo = max(abs(pasos))
    maximos.append(maximo)
    caminatas.append(pasos)
    
minimo = min(maximos)
maximo = max(maximos)

for caminata in caminatas:
    
    if max(abs(caminata)) == maximo:
       cam_max = caminata
    if max(abs(caminata)) == minimo:
       cam_min = caminata
       
fig = plt.figure()
plt.subplot(2, 1, 1) 
plt.plot(caminatas)
plt.title('Caminatas')

plt.subplot(2, 2, 3)

plt.plot(cam_max, label = 'Caminata Maxima')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(cam_min, label = 'Caminata mínima')
plt.legend()
plt.show()