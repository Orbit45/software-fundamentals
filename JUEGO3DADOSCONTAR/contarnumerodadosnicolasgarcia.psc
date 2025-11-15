Proceso ContarNumerosDadoNicolasGarcia
	
    Definir veces, i, dado Como Entero
    Definir c1, c2, c3, c4, c5, c6 Como Entero
	
    Escribir "¿Cuantas veces desea lanzar el dado?"
    Leer veces
	
    
    c1 <- 0
    c2 <- 0
    c3 <- 0
    c4 <- 0
    c5 <- 0
    c6 <- 0
	
    Para i <- 1 Hasta veces Con Paso 1 Hacer
        dado <- Aleatorio(1,6)
		
       
        Si dado = 1 Entonces
            c1 <- c1 + 1
        FinSi
		
        Si dado = 2 Entonces
            c2 <- c2 + 1
        FinSi
		
        Si dado = 3 Entonces
            c3 <- c3 + 1
        FinSi
		
        Si dado = 4 Entonces
            c4 <- c4 + 1
        FinSi
		
        Si dado = 5 Entonces
            c5 <- c5 + 1
        FinSi
		
        Si dado = 6 Entonces
            c6 <- c6 + 1
        FinSi
		
    FinPara
	
   
    Escribir "----- RESULTADO DE LOS LANZAMIENTOS -----"
    Escribir "El numero 1 salio: ", c1, " veces."
    Escribir "El numero 2 salio: ", c2, " veces."
    Escribir "El numero 3 salio: ", c3, " veces."
    Escribir "El numero 4 salio: ", c4, " veces."
    Escribir "El numero 5 salio: ", c5, " veces."
    Escribir "El numero 6 salio: ", c6, " veces."
	
FinProceso
