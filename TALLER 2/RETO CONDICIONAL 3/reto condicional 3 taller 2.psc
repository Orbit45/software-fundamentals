algoritmo clasificacioncompleta
    // 1. el cajon: definir la variable para guardar el numero
	// Recordatorios para examen Nicoals Seastian Garcia Moran.
    definir num como entero;
	
    // 2. aqui pide el dato
    escribir "escribe un numero entero positivo o negativo:";
    leer num;
	
    // 3. rombo principal si estuvieramos en el flowgori...: es positivo o negativo? 
    si (num >= 0) entonces
        //  rama positivos/cero verdadero
		
        // rombo 1: es el cero?
        si (num = 0) entonces
            escribir "el numero es cero.";
        sino
            // rombo 2: es par o impar? (para los positivos)
            si (num mod 2 = 0) entonces
                escribir "el numero ", num, " es par positivo.";
            sino
                escribir "el numero ", num, " es impar positivo.";
            finsi
        finsi
    sino
        // rama negativos falsa
		
        // rombo anidado 3: es par o impar? (para los negativos)
        // RECORDATORIO PARA EXAMEN IMPORTANTE USAR ABS "usamos abs() para que el mod funcione bien con negativos."
        si (abs(num) mod 2 = 0) entonces
            escribir "el numero ", num, " es par negativo.";
        sino
            escribir "el numero ", num, " es impar negativo.";
        finsi
    finsi
finalgoritmo

