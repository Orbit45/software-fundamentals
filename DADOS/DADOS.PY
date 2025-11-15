# Nicolas Sebastian Garcia Moran

print("******* Digite un numero: ******* ")
entrada = input()


if entrada.startswith("-"):
    sin_signo = entrada[1:]
else:
    sin_signo = entrada


if sin_signo.isdigit():
    numero = int(entrada)

    
    if (numero // 2) * 2 == numero:
        print("El numero es par...")
    else:
        print("El numero es impar...")
else:
    print("Error Solo se puede escribir numeros (pueden ser grandes o negativos).")
