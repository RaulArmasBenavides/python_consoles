
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
