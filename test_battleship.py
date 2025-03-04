#test Battleship
#Crea la clase Ship:
#Define el constructor __init__ que reciba name y size como parámetros.
#Agrega atributos: self.name, self.size, self.positions (una lista vacía para 
# las posiciones del barco) y self.hits (inicializado en 0).


class ship:
    def __init__(self, name, size):
        self.name= name
        self.size= size
        self.positions= []
        self.hits= 0


#Método place_ship:
#Este método coloca el barco en el tablero (board) según la posición 
# inicial (start_row, start_col) y la dirección (direction).
#Verifica si el barco cabe en el tablero. Si no cabe, devuelve False.
#Si la posición está libre (' '), almacena las posiciones en la
# lista positions. Si no, devuelve False.
#Actualiza el tablero con el símbolo del barco (self.name[0]), 
# almacena las posiciones en self.positions, y devuelve True.

    def place_ship(self, board, start_row, start_col, direction):
        positions= []  #porque se pone otra vez positions?
        if direction== "H":  
            if start_col + self.size > len(board[0]): #porque se usa self.size y no size?
                return False
            for i in range(self.size): #porque se usa self.size y no size?
                if board[start_row][start_col + i] != " ": #porque no lleva coma entre corchetes?
                    return False
                positions.append((start_row,start_col + i))
        elif direction == "V":
            if start_row + self.size > len(board):
                return False
            for i in range(self.size):
                if board[start_row + i][start_col] != " ": 
                    return False
                positions.append((start_row + i)(start_col))
        else:
            return False
        
        for pos in positions:
            board[pos[0]][pos[1]] = self.name[0]
        self.positions = positions
        return True

#Método hit:
#Incrementa el contador self.hits.
#Devuelve True si el número de impactos (self.hits) es igual al 
# tamaño del barco (self.size), indicando que el barco ha sido hundido.
    def hit(self):
        self.hits += 1
        return self.hits == self.size #creo que no hace todo lo que indica la instrucción
           

#Crea las subclases:
#Crea una clase Destroyer que herede de Ship y tenga un tamaño de 2.
#Crea una clase Submarine que herede de Ship y tenga un tamaño de 3.
#Crea una clase Battleship que herede de Ship y tenga un tamaño de 4.

class destroyer(ship):
    def __init__(self):
        super().__init__("Destructor", 2)

class submarine(ship):
    def __init__(self):
        super().__init__("Submarino", 3)

class battleship(ship):
    def __init__(self):
        super().__init__("Acorazado", 4)

#Crea la clase Player:
#Define el constructor __init__ que reciba name como parámetro.
#Crea un tablero self.board de 10x10, representado por una lista de listas, 
# inicializado con espacios en blanco ' '.
#Crea una lista self.ships para almacenar los barcos del jugador.
#Crea un segundo tablero self.hits para registrar los ataques.

class player:
    def __init__(self, name):
        self.name = name
        self.board = [[" " for _ in range(10)] for _ in range(10)] #no entendí este comando
        self.ships = []
        self.hits = [[" " for _ in range(10)] for _ in range(10)]


#Método place_ships:
#Crea instancias de Destroyer, Submarine y Battleship.
#Para cada barco, pide al jugador que ingrese la fila, columna 
# y dirección (H para horizontal, V para vertical) donde desea colocar el barco.
#Llama a place_ship para intentar colocar el barco. 
# Si no es posible, solicita nuevamente la entrada del usuario.

    def place_ships(self):
        ships= [destroyer(), submarine(), battleship()]
        for ship in ships:
            while True:
                print:(f"{self.name}, coloca tu {ship.name} de tamaño {ship.size}.") #porque lleva dos puntos despues del print
                start_row = int(input("Fila inicial: "))
                start_col = int(input("Columna inicial: "))
                direction = input("Dirección (H para horizontal, V para vertical): ").upper
                if ship.place_ship(start_row, start_col, direction, self.board): #en el if se crea una variable?
                    self.ships.append(ship)
                    self.print_board(self.board)
                    break
                else:
                    print("Posición no válida. Inténtalo de nuevo")

#Método print_board:
#Imprime el tablero de juego para mostrar la posición actual de los 
# barcos o los impactos.
    
    def print_board(self, board):
        for row in board:
            print("".join(row))
        print()


#Método attack:
#Solicita al jugador la fila y columna para atacar.
#Verifica si la posición es válida y si el ataque es un impacto o agua.
#Actualiza el tablero del oponente y el tablero de impactos del jugador 
# en consecuencia.
#Si se impacta un barco, verifica si ha sido hundido.

    def attack(self, opponent):
        while True:
            print(f"{self.name}, elige una posición para atacar")
            row = int(input("Fila: "))
            col = int(input("Columna: "))
            if 0 <= row < 10 and 0 <= col < 10:
                if opponent.board[row][col]  == " ":
                    print("Agua")
                    self.hits[row][col] = "W"
                    opponent.board[row][col] = "W"
                    break
                elif opponent.board[row][col] != "W": #como sabe opponen.board que tiene una A, si se guardó en self.hits
                    print("Impacto")
                    self.hits[row][col] = "T"
                    for ship in opponent.ships:
                        if (row, col) in ship.positions:
                            if ship.hit():
                                print(f"Hundido Has hundido el {ship.name}.")
                                break
                    opponent.board[row][col] = "T"
                    break
                else:
                    print("Ya has atacado esta posición previamente. Intenta de nuevo")        
            else: 
                print("Posición no válida. Intenta de nuevo")   

#Método all_ships_sunk:
#Devuelve True si todos los barcos del jugador han sido hundidos.

    def all_ships_sunk(self):
        return all(ship.hits == ship.size for ship in self.ships) #no entendé este comando
    
#Crea la clase BattleshipGame:
#Define el constructor __init__ que inicialice dos jugadores (player1 y player2).
#Método play:
#Pide a cada jugador que coloque sus barcos en el tablero.
#Alterna turnos entre los jugadores para atacar el tablero del oponente.
#Finaliza el juego cuando todos los barcos de un jugador han sido hundidos, 
# declarando al otro jugador como ganador.    
    
class Battleshipgame:

    def __init__(self):
        self.player1 = player("Jugardor 1")
        self.player2 = player("Jugador 2")

    def play(self):
        print("Bienvenido al juego de Batalla Naval")
        print("Jugador 1 coloca sus barcos")
        self.player1.place_ships()
        print("Jugador 2 coloca sus barcos")
        self.player2.place_ships()

        current_player = self.player1
        opponent = self.player2

        while True:
            current_player.attack(opponent)
            if opponent.all_ships_sunk():
                print(f"{current_player.name} ha ganado el juego")
                break
            current_player, opponent = opponent, current_player # esto para que se hace
            
game = Battleshipgame()
game.play()