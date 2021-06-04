#Actividad 1, ejercicio 2 
#Grafique en Python las siguientes funciones, f(x) = x^2-x+1, g(x) = 2/x-1
# Grafique ambas funciones en el mismo gráfico.

#importo las librerias necesarias para poder graficar 
import matplotlib.pyplot as plt
import numpy as np

#escribo las funciones a graficar
# le asigno nombres a cada una de las  graficas, esto me
#permitira tener claro sus valores al momento de utilizar 
#los comandos  para graficar 
f= lambda x: (x**2)-x+1
g= lambda x: 2/(x-1)

#escribo los valores tanto para x, y y los intervalos entre ellos
x=np.linspace(-5,5,200)
grafica1=f(x)
grafica2=g(x)

#grafico las funciones 
# color me sirve para dar colores a cada grafica
#  en este caso utilizo los colores azul y amarillo
plt.plot(x,grafica1, color="blue")
plt.plot(x,grafica2, color="yellow")

# el siguiente comando es el que me va a ayudar a mostrar las graficas
plt.show()
