import random
import keyboard

position_1 = 0

def go_ladder(pos=0):
    escalera = {3:11, 10:12, 9:18, 6:17}
    if pos in escalera.keys():
        print('Casilla Escalera ')
        return escalera[pos]                 
    else:
        return pos

def go_snakes(pos=0):
    serpientes = {22:20, 19:8, 14:4, 24:16}
    if pos in serpientes.keys():
        print('Casilla Serpientes -_-')
        return serpientes[pos]
        
    else:
        return pos

def roll_dice():
    dado = random.randint(1,6)
    return dado

def winning(posicion_actual):
    if posicion_actual >= 25:
        return True
    else:
        return False

while True:
    print('Presiona barra espaciadora para lanzar el dado')
    keyboard.wait(' ')
    dado = roll_dice()
    print(f'dado arroja: {dado}')
    position_actual=dado+position_1
    position_1 = go_ladder(position_actual)
    position_1 = go_snakes(position_actual)
    print(f'jugador avanza cuadro : {position_1}')
    if winning(position_1):
        print("Ganaste")
        break

