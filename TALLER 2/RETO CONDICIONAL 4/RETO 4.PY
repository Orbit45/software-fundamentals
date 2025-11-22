try:
    num1 = float(input("ingresa el primer numero num1: "))
    num2 = float(input("ingresa el segundo numero num2: "))
except ValueError:
    print("error: por favor, ingresa solo valores numericos")
    exit()

print("\n--- menu de operaciones ---")
print("[1]. sumar")
print("[2]. restar")
print("[3]. multiplicar")
print("[4]. dividir")
print("[5]. todas las operaciones")

try:
    opcion = int(input("elige una opcion (1-5): "))
except ValueError:
    print("error: la opcion debe ser un numero entero")
    exit()

if opcion == 1:
    resultado = num1 + num2
    print(f"\nresultado de la suma: {resultado}")

elif opcion == 2:
    resultado = num1 - num2
    print(f"\nresultado de la resta: {resultado}")

elif opcion == 3:
    resultado = num1 * num2
    print(f"\nresultado de la multiplicacion: {resultado}")

elif opcion == 4:
    if num2 == 0:
        print("\nerror: division por cero no permitida")
    else:
        resultado = num1 / num2
        print(f"\nresultado de la division: {resultado}")

elif opcion == 5:
    print("\n--- resultados de todas las operaciones ---")
    print(f"suma: {num1 + num2}")
    print(f"resta: {num1 - num2}")
    print(f"multiplicacion: {num1 * num2}")
    
    if num2 == 0:
        print("division: error (divisor cero)")
    else:
        print(f"division: {num1 / num2}")

else:
    print("\nopcion no valida. por favor, elige un numero del 1 al 5")