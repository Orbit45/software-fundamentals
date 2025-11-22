#NICOLAS GARCIA
tipo_identificacion = input("ingresa tipo de identificacion (cc, ps, ce, ci): ").lower()
nombres = input("ingresa nombres: ").lower()
apellidos = input("ingresa apellidos: ").lower()
genero = input("ingresa genero (m para mujer, h para hombre): ").lower()
anio_nacimiento = input("ingresa anio de nacimiento: ")
direccion = input("ingresa direccion: ").lower()
telefono = input("ingresa telefono: ")
salario = float(input("ingresa salario actual: "))


incremento = 0.0


if salario <= 1200000:
    if genero == "m":
        incremento = 0.10
    elif genero == "h":
        incremento = 0.08
    
elif salario > 1200000 and salario < 2000000:
    incremento = 0.05

elif salario >= 2000000:
    if genero == "m":
        incremento = 0.03
    elif genero == "h":
        incremento = 0.025


salario_final = salario * (1 + incremento)


print("\n--- datos del usuario ---")
print(f"nombre: {nombres} {apellidos}")
print(f"identificacion: {tipo_identificacion}")
print(f"genero: {genero}")
print(f"salario inicial: {salario:.2f}")
print(f"incremento aplicado: {incremento * 100:.1f}%")
print(f"salario final: {salario_final:.2f}")