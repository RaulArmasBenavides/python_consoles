#TEMA : CIENCIA DE DATOS REGRESIÓN LINEAL
"""
Elabore un programa en Python que elabore un diagrama de dispersión de datos X (°F) e Y (Espuma %), 
póngalos un diagrama de dispersión, luego calcule la recta de correlación cuya formula es: 
y luego debe responder a estimar el porcentaje de espuma con los °F que le brinde el usuario. 
Debe solicitar el número de puntos a correlacionar y empleando todo lo enseñado en clase. 
Considere como ejemplo el siguiente caso: 
determine si existe una relación entre las temperaturas del producto y el porcentaje de espuma en una bebida refrescante. 
Los datos son los siguientes:
a) Realice los análisis de correlación correspondiente con los datos mostrados.

b) ¿Qué porcentaje de espuma se tiene a los 35 y 52 °F? Sustente su respuesta

     Se pide:

(5p) Elabore el código en Python correspondiente empleando funciones y librerías enseñadas en clases.

(2p) Elabore un histograma mensual de horas y del total anual por cajero
"""

# shows how linear regression analysis can be applied to 1-dimensional data

from __future__ import print_function, division
from builtins import range
# Note: you may need to update your version of future
# sudo pip install -U future
import numpy as np
import matplotlib.pyplot as plt



# si la data está parametrizada en un excel
X = []
Y = []
for line in open('data_1d.csv'):
    x, y = line.split(',')
    X.append(float(x))
    Y.append(float(y))

# let's turn X and Y into numpy arrays since that will be useful later
X = np.array(X)
Y = np.array(Y)


# Gráfico de dispersión
plt.scatter(X, Y)
plt.title('Relación entre temperatura y espuma', fontsize=15)
plt.xlabel('Fº')
plt.ylabel('Espuma')
plt.show()


# mínimos cuadrados
denominator = X.dot(X) - X.mean() * X.sum()
a = ( X.dot(Y) - Y.mean()*X.sum() ) / denominator
b = ( Y.mean() * X.dot(X) - X.mean() * X.dot(Y) ) / denominator


Yhat = a*X + b


plt.title('Tendencias', fontsize=15)
plt.xlabel('Fº')
plt.ylabel('Espuma')
plt.scatter(X, Y)
plt.plot(X, Yhat)
plt.show()

# determine how good the model is by computing the r-squared
d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)
print("r-squared es:", r2)
