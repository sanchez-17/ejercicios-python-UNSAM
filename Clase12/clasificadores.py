# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

'''Ejercicio 12.12

Repetí 100 veces lo siguiente y calculá el promedio de los scores:

a) Partición del conjunto original en test y train aleatoriamente (sin fijar la semilla).

b) Entrenamiento de ambos modelos (knn y clf) con el conjunto train resultante.

c) Evaluación de ambos clasifcadores (score) con el conjunto test resultante.

    Imprimí el promedio de los scores obtenidos
'''

iris_dataset = load_iris()

res_knn , res_clf, res_rfc = [],[],[]

for i in range(100):
    #Separamos los datos en 2 oonjuntos aleatoriamente
    X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'])
    #Entreno el clasificador knn y lo evalúo
    knn = KNeighborsClassifier(n_neighbors = 1)
    knn.fit(X_train, y_train)

    res_knn.append(knn.score(X_test, y_test))
    
    #Entreno el clasificador clf y lo evalúo
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    res_clf.append(clf.score(X_test, y_test))
    
    #Entreno el clasificador rfc y lo evalúo
    rfc = RandomForestClassifier(max_depth=3)
    rfc.fit(X_train, y_train)

    res_rfc.append(rfc.score(X_test, y_test))
print(f"Resultados:\nKNN:{np.mean(res_knn):0.2f}\nCLF:{np.mean(res_clf):.2f}\nRFC:{np.mean(res_rfc):.2f}")