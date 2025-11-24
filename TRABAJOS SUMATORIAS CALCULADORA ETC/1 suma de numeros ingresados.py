acumulador = 0
status = True
while status:
    print("Ingresa varios numeros para la suma ( (0) para salir):")
    num = int(input())
    acumulador += num
    if num == 0:
        status = False

print(f"Total de suma de numeros ingresados: {acumulador}")
#Total de suma de numeros ingresados
