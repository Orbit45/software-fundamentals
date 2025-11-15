Proceso LanzarDadosConReporteNicolasSebastianGarciaMoran
	
    Definir dado, totalTiros, suma, pares, impares Como Entero
    Definir respuesta Como Cadena
	
    totalTiros <- 0
    suma <- 0
    pares <- 0
    impares <- 0
	
    Repetir
        dado <- Aleatorio(1,6)
        Escribir "Dado generado: ", dado
		
        totalTiros <- totalTiros + 1
        suma <- suma + dado
		
        Si (dado / 2) * 2 = dado Entonces
            pares <- pares + 1
        Sino
            impares <- impares + 1
        FinSi
		
        Escribir "¿Desea lanzar de nuevo? (si/no)"
        Leer respuesta
		
    Hasta Que respuesta <> "si"
	
    Escribir "----- REPORTE FINAL -----"
    Escribir "Total de tiros efectuados: ", totalTiros
    Escribir "Suma total de los tiros: ", suma
    Escribir "Total de pares generados: ", pares
    Escribir "Total de impares generados: ", impares
	
FinProceso
