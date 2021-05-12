# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

## Lectura de las coordenadas de los puntos del mallado.

f = open("lista_puntos.txt")

num_punt = int(f.readline())

coord = np.zeros((num_punt,2))

for i in range(num_punt):
    c = f.readline()
    c = c.split()
    coord[i,0] = float(c[0])
    coord[i,1] = float(c[1])

f.close()

# Lectura de los vertices de los triangulos del mallado.

g = open("enlaces.txt")

num_enlaces = int(g.readline())

vertices = np.zeros((num_enlaces, 3))

for j in range(num_enlaces):
    d = g.readline()
    d = d.split()
    for k in range(3):
        vertices[j, k] = float(d[k])           ## Conversion de cadena de caracteres a float. No deja convertirlo directamente a entero.

g.close()

# Convertimos a entero.
vertices = vertices.astype(int)

print("Puntos del mallado")
print(coord)
print("Puntos de cada triangulo")
print(vertices)


colours = ["b", "g", "r", "c", "m", "y", "tab:cyan", "tab:orange"]       ## Colores a usar para cada linea.

plt.plot(coord[:,0], coord[:,1], "o")         ## Coordenadas x vs coordenadas y


for i in range(num_enlaces):
    plt.plot([coord[vertices[i, 0], 0], coord[vertices[i, 1], 0]], [coord[vertices[i, 0], 1] ,coord[vertices[i, 1], 1]], color=colours[i])
    plt.plot([coord[vertices[i, 1], 0], coord[vertices[i, 2], 0]], [coord[vertices[i, 1], 1], coord[vertices[i, 2], 1]], color=colours[i])
    plt.plot([coord[vertices[i, 2], 0], coord[vertices[i, 0], 0]], [coord[vertices[i, 2], 1], coord[vertices[i, 0], 1]], color=colours[i])

plt.xlabel("Coordenadas x del mallado")
plt.ylabel("Coordenadas y del mallado")
plt.title("Mallado")

plt.show()
