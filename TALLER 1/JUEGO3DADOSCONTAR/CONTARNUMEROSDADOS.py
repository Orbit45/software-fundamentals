import random

print("¿Cuantas veces desea lanzar el dado?")
veces = int(input())

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0

for i in range(veces):
    dado = random.randint(1, 6)
    if dado == 1:
        c1 += 1
    if dado == 2:
        c2 += 1
    if dado == 3:
        c3 += 1
    if dado == 4:
        c4 += 1
    if dado == 5:
        c5 += 1
    if dado == 6:
        c6 += 1

print("----- RESULTADO DE LOS LANZAMIENTOS -----")
print("El numero 1 salio:", c1, "veces.")
print("El numero 2 salio:", c2, "veces.")
print("El numero 3 salio:", c3, "veces.")
print("El numero 4 salio:", c4, "veces.")
print("El numero 5 salio:", c5, "veces.")
print("El numero 6 salio:", c6, "veces.")
