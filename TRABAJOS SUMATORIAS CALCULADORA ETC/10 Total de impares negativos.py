impares_negativos = 0

while True:
    n = int(input("Ingrese un número (0 para terminar): "))
    if n == 0:
        break
    if n < 0 and n % 2 != 0:
        impares_negativos += 1

print("Total de impares negativos:", impares_negativos)
