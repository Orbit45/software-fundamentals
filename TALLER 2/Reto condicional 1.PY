import random
import os
os.system('cls' if os.name == 'nt' else 'clear')
random.seed() 
print("####### Nombre: Nicolas Sebastian Garcia Moran #######\n")
dado1 = int(random.random() * 6 )
dado2 = int(random.random() * 6 )
print ("                     El dado 1 es: " + str (dado1))
print ("                     El dado 2 es: " + str (dado2))
if dado1 == dado2:
    print ("\n                 GANASTE")
    print (dado1 == dado2)
else:
    print ("\n                 GAME OVER")
    print (dado1 == dado2)
if dado1 % 2 == 0:
    print ("                     Dado 1 es: Par")
else:
    print ("                     Dado 1 es: impar")
if dado2 % 2 == 0:            
    print("                     Dado 2 es: par")
else:
    print("                     Dado 2 es: impar")
print ("\n####### Gracias por Jugar :D #######")        