"""
Brayan Pineda Méndez - Lunes 14 de diciembre del 2020
Crear un grafico 2D
18390039
"""
import numpy as np
import matplotlib.pyplot as plt

#Se crea el cuadro donde se mostrará los graficos
plt.axis([-100, 200, -100, 200])
plt.axis('on')
plt.grid(True)
plt.title('Examen 2D')

#Centro del circulo
xc = 50
yc = 50

#Radio del circulo dado por el último número del número de control
r = 9*5

p1 = 0 * np.pi/180 #Punto de inicio del círculo
p2 = 360 * np.pi/180#Punto de Final del círculo
dp = (p2 - p1)/180 #Diametro del circulo dado por el inicio y el final del circulo

xlast = xc + r*np.cos(p1)
ylast = yc + r*np.sin(p1)

color = [0/10, 3/10, 9/10]

#Se dibuja el círculo mediante un for
for p in np.arange(p1, p2+dp, dp):
    xp = xc + r * np.cos(p)
    yp = yc + r * np.sin(p)
    plt.plot([xlast, xp], [ylast, yp], color=color)
    xlast = xp
    ylast = yp


#Para el segundo rectángulo se utiliza como referencia el centro de las coordenadas multiplciando por el radio
x = np.array([xc, xc, xc+2*r, xc+2*r, xc])
y = np.array([yc, yc-2*r, yc-2*r, yc, yc])
plt.plot(x, y, color=color)

#Para el primer rectángulo se multiplica el centro para que quede en el centro, utilizando el mismo código que se usó para el segundo rectángulo
xc *= 1.9
yc *= 1.9
x = np.array([xc, xc, xc-2*r, xc-2*r, xc])
y = np.array([yc, yc-2*r, yc-2*r, yc, yc])
plt.plot(x, y, color=color)

plt.show()