algoritmo calculadoraconmenu
	// Nicolas Sebastian Garcia Moran
    definir num1, num2 como real;
    definir opcion como entero;
	
    escribir "ingresa el primer numero (num1):";
    leer num1;
    escribir "ingresa el segundo numero (num2):";
    leer num2;
	
    escribir "";
    escribir "--- menu de operaciones ---";
    escribir "[1]. sumar";
    escribir "[2]. restar";
    escribir "[3]. multiplicar";
    escribir "[4]. dividir";
    escribir "[5]. todas las operaciones";
	
    escribir "elige una opcion (1-5):";
    leer opcion;

    si opcion = 1 entonces
        escribir "resultado de la suma: ", num1 + num2;
    sino
    
        si opcion = 2 entonces
            escribir "resultado de la resta: ", num1 - num2;
        sino
        
            si opcion = 3 entonces
                escribir "resultado de la multiplicacion: ", num1 * num2;
            sino
              
                si opcion = 4 entonces
                    si num2 = 0 entonces
                        escribir "error: division por cero no permitida";
                    sino
                        escribir "resultado de la division: ", num1 / num2;
                    finsi 
                sino
                    
                    si opcion = 5 entonces
                        escribir "--- resultados de todas las operaciones ---";
                        escribir "suma: ", num1 + num2;
                        escribir "resta: ", num1 - num2;
                        escribir "multiplicacion: ", num1 * num2;
                        
                        si num2 = 0 entonces
                            escribir "division: error (divisor cero)";
                        sino
                            escribir "division: ", num1 / num2;
                        finsi 
                    sino
                        
                        escribir "opcion no valida. por favor, elige un numero del 1 al 5";
                    finsi 
                finsi 
            finsi 
        finsi 
    finsi 
    
finalgoritmo