pares_pos = 0

print("Ingrese números. 0 para terminar.")

while True:
    n = int(input("Número: "))

    if n == 0:   # no se cuenta, solo termina
        break

    if n > 0 and n % 2 == 0:
        pares_pos += 1

print("Total de pares positivos:", pares_pos)
