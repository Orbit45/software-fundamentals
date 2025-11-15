Proceso ContarParesImparesNicolasGarcia
	
    Definir n, i, dado, pares, impares Como Entero
	
    Escribir "¿Cuántos lanzamientos desea realizar?"
    Leer n
	
    pares <- 0
    impares <- 0
	
    Para i <- 1 Hasta n Con Paso 1 Hacer
        dado <- Aleatorio(1,6)
		
        Si (dado / 2) * 2 = dado Entonces
            pares <- pares + 1
        Sino
            impares <- impares + 1
        FinSi
    FinPara
	
    Escribir "Tiros pares: ", pares
    Escribir "Tiros impares: ", impares
	
FinProceso
