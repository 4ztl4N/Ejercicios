matrix = [[1,2,3], 
          [4,5,6], 
          [7,8,9]]
print(matrix)
print(matrix[0])
print(matrix[2][1])
numbers = (1,2,3,4,5)
print(numbers)
print(type(numbers))
print(numbers[0])
#numbers[0] = "unos"
#print(numbers)

#Un tablero de ajedrez es una matriz de 8x8. En vez de representar 
# solo las casillas blancas y negras, podemos representar las piezas
#  de ajedrez. Usaremos letras para representar las piezas: P para 
# peón, R para torre, N para caballo (knight), B para alfil, 
# Q para reina y K para rey. Las piezas negras se representan 
# con letras minúsculas y las blancas con letras mayúsculas.
chess_board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

print(chess_board)

#Si movemos el caballo de (7, 1) a (5, 2), el tablero se vería así:
chess_board[7][1] = 0  # Casilla original del caballo ahora está vacía
chess_board[5][2] = 'N'  # Nueva posición del caballo

print(chess_board)

#Un tablero de damas también es una matriz de 8x8, pero además 
# de las casillas alternas, debemos representar las piezas 
# de los dos jugadores.
checkers_board = [
    [0, 'b', 0, 'b', 0, 'b', 0, 'b'],
    ['b', 0, 'b', 0, 'b', 0, 'b', 0],
    [0, 'b', 0, 'b', 0, 'b', 0, 'b'],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ['w', 0, 'w', 0, 'w', 0, 'w', 0],
    [0, 'w', 0, 'w', 0, 'w', 0, 'w'],
    ['w', 0, 'w', 0, 'w', 0, 'w', 0]
]

print(checkers_board)

#Las matrices también son esenciales para la representación y
#  manipulación de imágenes. Cada píxel de una imagen en escala
#  de grises se puede representar como un valor en una matriz, 
# donde cada valor varía del 0 (negro) al 255 (blanco).
image = [
    [255, 0, 0, 0, 255],
    [0, 255, 0, 255, 0],
    [0, 0, 255, 0, 0],
    [0, 255, 0, 255, 0],
    [255, 0, 0, 0, 255]
]

print(image)