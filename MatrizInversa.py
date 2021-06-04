#Actividad 1, ejercicio 1
# Desarrolle en Python un programa para calcular la inversa de matrices de dimensión 2x2. 
# No olvide colocar comentarios en su programa. No busque el programa en internet.


# importo la libreria numpy 
import numpy as np

# ingreso mediante teclado los valores 
# para la matriz a invertir
print("Ingrese los valores de la matriz: ")
a=float(input("Ingrese el valor de a: "))
b=float(input("Ingrese el valor de b: "))
c=float(input("Ingrese el valor de c: "))
d=float(input("Ingrese el valor de d: "))

#calculo la matriz inversa
matriz =np.array([[a,b],[c,d]])
mInverza =np.linalg.inv(matriz)

#muestro la matriz original
print("La matriz a invertir es: ")
print(matriz)

#muestro la matriz inversa 
print("La matriz invertida es: ")
print(mInverza)