import random

while True:
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    print("Dado 1:", d1, " Dado 2:", d2)
    if d1 == 6 and d2 == 6:
        print("¡Par de SEIS generado!")
        break
