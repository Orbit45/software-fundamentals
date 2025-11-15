import random

n = int(input("¿Cuántos lanzamientos desea realizar?: "))

pares = 0
impares = 0

for i in range(n):
    dado = random.randint(1, 6)
    if dado % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Tiros pares:", pares)
print("Tiros impares:", impares)
