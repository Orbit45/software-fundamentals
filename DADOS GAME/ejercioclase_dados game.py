import os
from random import randint

lives = 3
suma = 0
wins = 0
losses = 0

def roll_dice():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    return dice1, dice2

while True:
    input('presiona cualquier tecla para lanzar los dados: ')
    dice1, dice2 = roll_dice()
    print(f'dado1: {dice1}')
    print(f'dado2: {dice2}')
    suma += 1

    if (dice1 + dice2) % 2 == 0:
        lives = 3
    else:
        lives -= 1

    if dice1 == 6 and dice2 == 6:
        print('ganaste')
        print('total de lanzamientos:', suma)
        wins += 1
        break

    if lives == 0:
        print('game over')
        print('total de lanzamientos:', suma)
        losses += 1
        break

print('---------------------------------')
print('resultados finales')
print(f'veces que ganaste: {wins}')
print(f'veces que perdiste: {losses}')
print('---------------------------------')
