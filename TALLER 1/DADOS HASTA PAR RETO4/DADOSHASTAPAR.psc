Proceso DadosHastaParDeSeisNicolasGarcia
    Definir d1, d2, n, i, terminado Como Entero
    terminado <- 0
	
    Escribir "Cuantas veces desea lanzar los dados?"
    Leer n
	
    Repetir
        Para i <- 1 Hasta n Con Paso 1 Hacer
            d1 <- Aleatorio(1,6)
            d2 <- Aleatorio(1,6)
			
            Escribir "Dado 1: ", d1, "  Dado 2: ", d2
			
            Si d1 = 6 Y d2 = 6 Entonces
                Escribir "¡Par de SEIS generado!"
                terminado <- 1
            FinSi
        FinPara
    Hasta Que terminado = 1
FinProceso
