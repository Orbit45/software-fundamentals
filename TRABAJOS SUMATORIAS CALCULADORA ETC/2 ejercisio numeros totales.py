contador = 0

while True:
    n = int(input("Ingrese un número (0 para terminar): "))
    if n == 0:
        break
    contador += 1

print("Total de números ingresados:", contador)
