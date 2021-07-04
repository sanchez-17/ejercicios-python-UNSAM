# -*- coding: utf-8 -*-
"""
Created on Sun May  2 01:43:50 2021

@author: Gaston
"""
import matplotlib.pyplot as plt
import numpy as np

term = np.load('../Data/Temperaturas.npy')

plt.hist(term,bins=22, density=True)
plt.show()