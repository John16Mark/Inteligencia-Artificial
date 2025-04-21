N = 4

def es_seguro(tablero, fila, col):
    for i in range(col):
        if tablero[fila][i] == 1:
            return False
    
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False
    
    for i, j in zip(range(fila, N, 1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False
    
    return True

def resolver_n_reinas(tablero, col):
    if col >= N:
        return True
    
    for i in range(N):
        if es_seguro(tablero, i, col):
            tablero[i][col] = 1
            if resolver_n_reinas(tablero, col + 1):
                return True
            tablero[i][col] = 0
    
    return False

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join("Q" if x == 1 else "." for x in fila))
    print("\n")

def solucionar():
    tablero = [[0] * N for _ in range(N)]
    if resolver_n_reinas(tablero, 0):
        imprimir_tablero(tablero)
    else:
        print("No hay solución")

solucionar()