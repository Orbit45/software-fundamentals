Proceso LanzarDadoSumaJUEGONicolasGarcia
	
    Definir veces, i, dado, suma Como Entero
	escribir "Nicolas Sebastian Garcia Moran"
    escribir " Cuantas veces desea lanzar el dado? "
    leer veces
	
    suma <- 0
	
    Para i <- 1 Hasta veces Con Paso 1 Hacer
        dado <- Aleatorio(1,6)
        suma <- suma + dado
    FinPara
	
    Escribir "La suma total de los valores generados es: ", suma
	
FinProceso
