#Actividad 1, ejercicio 6 
#Diseñe un código que encuentre el sen(pi/3)
#a través del desarrollo de Taylor, truncar cuando n = 50.
#importo ñas librerias necesarias
import numpy as np
from numpy.lib import math
#Asugno el valor de la funcion
x=np.pi/3
#el valor hasta donde se va a realizar 
n=50
polinomio=0

for k in range(n):
    polinomio=polinomio + (-1)**k*x**(2*k+1) /np.math.factorial(2*k+1)
    print(k,polinomio)
