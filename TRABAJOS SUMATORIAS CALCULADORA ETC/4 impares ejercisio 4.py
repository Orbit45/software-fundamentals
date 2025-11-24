impares = 0

while True:
    n = int(input("Ingrese un número (0 para finalizar): "))
    if n == 0:
        break
    if n % 2 != 0:
        impares += 1

print("Total de impares dijitados por el usuaeio:", impares)
