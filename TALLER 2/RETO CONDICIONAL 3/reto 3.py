#RECORDATORIOS PARA EXAMEN NICOLAS GARCIA MORAN rombo para pasarlo en dado caso del examen guiarse con rombo para flowgorin...
# pedir el numero
num = int(input("escribe un numero entero positivo o negativo: "))

# rombo principal signos
if num >= 0:
    # rama positivos o cero
    
    # rombo cero
    if num == 0:
        print(f"el numero es cero.")
    
    # rombo par o impar positivos IMPORTANTE EL %%%%%
    else: 
        if num % 2 == 0:
            print(f"el numero {num} es par positivo.")
        else:
            print(f"el numero {num} es impar positivo.")

else:
    # rama negativos
    
    # rombo par o impar negativos
    if num % 2 == 0:
        print(f"el numero {num} es par negativo.")
    else:
        print(f"el numero {num} es impar negativo.")