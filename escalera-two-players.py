import random
import keyboard

def go_ladder(pos):
    escalera = {3:11, 10:12, 9:18, 6:17}
    if pos in escalera.keys():
        print('Casilla Escalera ')
        return escalera[pos]
    else:
        return pos

def go_snakes(pos):
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

jugadores = []
for i in range(2):
    nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
    jugador = {"nombre": nombre, "posicion": 0}
    jugadores.append(jugador)

while True:
    for jugador in jugadores:
        print('Presiona barra espaciadora para lanzar el dado')
        keyboard.wait(' ')
        dado = roll_dice()
        print(f'{jugador["nombre"]} tira el dado y obtiene: {dado}')
        jugador["posicion"] += dado
        jugador["posicion"] = go_ladder(jugador["posicion"])
        jugador["posicion"] = go_snakes(jugador["posicion"])
        print(f'{jugador["nombre"]} avanza a la casilla: {jugador["posicion"]}')
        if winning(jugador["posicion"]):
            print(f'{jugador["nombre"]} ha ganado!')
            break
    else:
        continue
    break
