import random

print("Nicolas Sebastian Garcia Moran")
print("Cuantas veces desea lanzar el dado?")
veces = int(input())

suma = 0

for i in range(veces):
    dado = random.randint(1, 6)
    suma = suma + dado

print("La suma total de los valores generados es:", suma)
