Algoritmo Dados
	
	
    Escribir "####### Nombre: Nicolas Sebastian Garcia Moran #######"
    Escribir ""
	
    // gera dados
    dado1 <- Aleatorio(0,5)
    dado2 <- Aleatorio(0,5)
	
    Escribir "                     El dado 1 es: ", dado1
    Escribir "                     El dado 2 es: ", dado2
	
    // aqui comapraaria los dadas
    Si dado1 = dado2 Entonces
        Escribir ""
        Escribir "                 GANASTE"
        Escribir (dado1 = dado2)
    Sino
        Escribir ""
        Escribir "                 GAME OVER"
        Escribir (dado1 = dado2)
    FinSi
	
    // par o impar del dado 1
    Si (dado1 % 2 = 0) Entonces
        Escribir "                     Dado 1 es: Par"
    Sino
        Escribir "                     Dado 1 es: Impar"
    FinSi
	
    // par o impar del dado 2
    Si (dado2 % 2 = 0) Entonces
        Escribir "                     Dado 2 es: Par"
    Sino
        Escribir "                     Dado 2 es: Impar"
    FinSi
	
    Escribir ""
    Escribir "####### Gracias por Jugar :D #######"
	
FinAlgoritmo

