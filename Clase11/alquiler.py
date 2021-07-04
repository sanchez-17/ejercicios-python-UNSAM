# -*- coding: utf-8 -*-
"""

"""
import numpy as np
import matplotlib.pyplot as plt

superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

g = plt.scatter(x = superficie, y = alquiler)
plt.title('gráfico de dispersión de los datos de alquiler')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#%%
def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

a, b = ajuste_lineal_simple(superficie, alquiler)

grilla_x = np.linspace(start = min(superficie), stop = max(superficie), num = 1000)
grilla_y = grilla_x*a + b

g = plt.scatter(x = superficie, y = alquiler)
plt.title('y ajuste lineal')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
#%%
print(f'\nCoeficientes:\n\nPendiente = {a}\nOrdenada al origen = {b}')
#%%

errores = alquiler - (a*superficie + b)
print('\nErrores:\n',errores)
print("ECM:", (errores**2).mean())