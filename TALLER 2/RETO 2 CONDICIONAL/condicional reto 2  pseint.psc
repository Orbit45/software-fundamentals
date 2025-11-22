Algoritmo ValidarParImpar
   
    Definir numero Como Entero;
    Escribir "Ingresa un número entero (positivo o negativo):";
    Leer numero;
    numero <- ABS(numero);
	
    Si (numero MOD 2 = 0) Entonces
        
        Escribir "El número ingresado es PAR.";
    SiNo
        
        Escribir "El número ingresado es IMPAR.";
    FinSi
	
FinAlgoritmo