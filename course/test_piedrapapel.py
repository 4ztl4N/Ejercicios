#opción 2
print("Bienvenidos a el juego piedra papel o tijeras")
print("Jugador 1 INGRESA TU NOMBRE:")
jugador_1 = input()
print("Jugador 2 INGRESA TU NOMBRE:")
jugador_2 = input()
print(jugador_1, "Qué elijes: piedra, papel o tijera?:")
jugador_1_movimiento = input(). lower()
print(jugador_2, "Qué elijes: piedra, papel o tijera?:")
jugador_2_movimiento = input(). lower()

validar = ["piedra", "papel", "tijera"]

if jugador_1_movimiento not in validar or jugador_2_movimiento not in validar:
    print("Uno o ambos jugadores hicieron una elección no válida, elijan solo piedra, papel o tijera")
else:
    if jugador_1_movimiento == jugador_2_movimiento:
        print("Empate")
    elif(jugador_1_movimiento == "piedra" and jugador_2_movimiento == "tijera") or\
        (jugador_1_movimiento == "tijera" and jugador_2_movimiento == "papel") or\
        (jugador_1_movimiento == "papel" and jugador_2_movimiento == "piedra"):
        print("GANA JUGADOR 1")
    else:
        print("GANA JUGADOR 2")
    
