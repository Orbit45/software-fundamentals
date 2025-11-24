
contador = 0
totalM = 0
totalF = 0
totalO = 0
totalSalario = 0
sumaEdades = 0

respuesta = "S"

while respuesta.upper() == "S": 
    nombre = input("Ingrese nombre completo del empleado: ")
    email = input("Ingrese email del empleado: ")
    telefono = input("Ingrese número móvil del empleado: ")
    
    genero = input("Ingrese el género (M/F/O): ").upper()
    while genero not in ["M", "F", "O"]:
        genero = input("Género inválido. Ingrese M, F u O: ").upper()
    
    salario = float(input("Ingrese salario del empleado: "))
    anioNacimiento = int(input("Ingrese año de nacimiento del empleado: "))
    
    edad = 2025 - anioNacimiento
    contador += 1
    totalSalario += salario
    sumaEdades += edad
    
    if genero == "M":
        totalM += 1
    elif genero == "F":
        totalF += 1
    else:
        totalO += 1
    
    respuesta = input("Desea agregar otro empleado? (S/N): ").upper()
    while respuesta not in ["S", "N"]:
        respuesta = input("Valor inválido. Ingrese S o N: ").upper()

promedioEdad = sumaEdades / contador if contador > 0 else 0

print("\n--- REPORTE DE EMPLEADOS ---")
print("Total de empleados:", contador)
print("Total de género M:", totalM)
print("Total de género F:", totalF)
print("Total de género O:", totalO)
print("Total de salario a pagar:", totalSalario)
print("Promedio de edades:", promedioEdad)
