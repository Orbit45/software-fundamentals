negativos = 0

while True:
    n = int(input("Ingrese un número (0 para terminar): "))
    if n == 0:
        break
    if n < 0:
        negativos += 1

print("Total de negativos ingresados:", negativos)
