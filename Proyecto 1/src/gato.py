import math
from lib.consola import gotoxy
from lib.diseno import colorForeground, customForeground, colorDefault

def revisar_victoria(tablero, jugada):
    victorias = [
        [0,1,2], [3,4,5], [6,7,8],  # filas
        [0,3,6], [1,4,7], [2,5,8],  # columnas
        [0,4,8], [2,4,6]            # diagonales
    ]
    for victoria in victorias:
        if tablero[int(victoria[0]/3)][victoria[0]%3] == tablero[int(victoria[1]/3)][victoria[1]%3] == tablero[int(victoria[2]/3)][victoria[2]%3] == jugada:
            return True
    return False

def es_empate(tablero):
    if(0 not in tablero[0] and 0 not in tablero[1] and 0 not in tablero[2]):
        return True
    return False

def minimax(tablero, profundidad, maximiza, imbatible):
    if(not imbatible):
        if revisar_victoria(tablero, 1):
            return 20 - profundidad
        elif revisar_victoria(tablero, 2):
            return -20 + profundidad
    else:
        if revisar_victoria(tablero, 1):
            return -20 + profundidad
        elif revisar_victoria(tablero, 2):
            return 20 - profundidad
    if es_empate(tablero):
        return 0
    
    if maximiza:
        mejor_puntaje = -math.inf
        for i in range(9):
            if tablero[int(i/3)][i%3] == 0:
                tablero[int(i/3)][i%3] = 2
                puntaje = minimax(tablero, profundidad + 1, False, imbatible)
                tablero[int(i/3)][i%3] = 0
                mejor_puntaje = max(puntaje, mejor_puntaje)
        return mejor_puntaje
    else:
        mejor_puntaje = math.inf
        for i in range(9):
            if tablero[int(i/3)][i%3] == 0:
                tablero[int(i/3)][i%3] = 1
                puntaje = minimax(tablero, profundidad + 1, True, imbatible)
                tablero[int(i/3)][i%3] = 0
                mejor_puntaje = min(puntaje, mejor_puntaje)
        return mejor_puntaje

def mejor_jugada(tablero, imbatible):
    mejor_puntuacion = -math.inf
    jugada = -1
    for i in range(9):
        if tablero[int(i/3)][i%3] == 0:
            tablero[int(i/3)][i%3] = 2
            puntaje = minimax(tablero, 0, False, imbatible)
            tablero[int(i/3)][i%3] = 0
            if puntaje > mejor_puntuacion:
                mejor_puntuacion = puntaje
                jugada = i
    return jugada

def imprimir_tablero(x, y):
    gotoxy(x+3, y)
    print("║", end='')
    gotoxy(x+7, y)
    print("║", end='')
    gotoxy(x, y+1)
    print("═══╬═══╬═══", end='')
    gotoxy(x+3, y+2)
    print("║", end='')
    gotoxy(x+7, y+2)
    print("║", end='')
    gotoxy(x, y+3)
    print("═══╬═══╬═══", end='')
    gotoxy(x+3, y+4)
    print("║", end='')
    gotoxy(x+7, y+4)
    print("║", end='')

def imprimir_jugada(tablero, x, y):
    for i in range (3):
        for j in range (3):
            casilla = tablero[i][j]
            gotoxy(x + j*4, y + i*2)
            if(casilla == 0):
                customForeground(60, 60, 60)
                print(" ", end='')
                print(i*3+j+1, end='')
            elif(casilla == 1):
                colorForeground("azul claro")
                print(" O", end = '')
            else:
                colorForeground("rojo claro")
                print(" X", end = '')
            colorDefault()
        print(" ")


def partida_3_raya(imbatible, x, y):
    tablero = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    imprimir_tablero(x, y)
    imprimir_jugada(tablero, x, y)

    while True:
        # Turno del jugador
        gotoxy(27, y+7)
        print("     ", end='')
        gotoxy(1, y+7)
        move = int(input("Elige tu movimiento (1-9): "))
        move -= 1
        if tablero[int(move/3)][move%3] != 0:
            gotoxy(1, y+6)
            print("\033[91mMovimiento inválido, intenta de nuevo.\033[0m", end='')
            continue
        gotoxy(1, y+7)
        print("                                         ")
        tablero[int(move/3)][move%3] = 1
        imprimir_jugada(tablero, x, y)

        if revisar_victoria(tablero, 1):
            gotoxy(56, y+9)
            print("\033[92m¡Ganaste!\033[0m", end='')
            break
        if es_empate(tablero):
            gotoxy(57, y+9)
            print("\033[0mEmpate.\033[0m", end='')
            break

        # Turno de la máquina
        gotoxy(1, y+7)
        print("Turno de la máquina (O):              ")
        move = mejor_jugada(tablero, imbatible)
        tablero[int(move/3)][move%3] = 2
        imprimir_jugada(tablero, x, y)

        if revisar_victoria(tablero, 2):
            gotoxy(55, y+9)
            print("\033[91m¡Perdiste!\033[0m", end='')
            break
        if es_empate(tablero):
            gotoxy(57, y+9)
            print("\033[0mEmpate.\033[0m")
            break