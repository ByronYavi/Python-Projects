from math import factorial
import matplotlib.pyplot as plt
import numpy as np
def numero_combinaciones(m, n):
    """Calcula y devuelve el número de combinaciones
       posibles que se pueden hacer con m elementos
       tomando n elementos a la vez.
    """
    return factorial(m) // (factorial(n) * factorial(m - n))


print(numero_combinaciones(25,3))
LISTA=[]
LISTA2=[]
for x in range(0,25):
   variable=numero_combinaciones(25,x)
   LISTA.append(variable)
   LISTA2.append(x)


fig, ax = plt.subplots()
ax.plot(LISTA2, LISTA)
plt.show()
