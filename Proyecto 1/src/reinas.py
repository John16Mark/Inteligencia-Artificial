from random import randint

debug = False

def contar_conflictos(N, tablero, x, y):
    conteo = 0
    i = 0
    while(i>=0 and i<N):
        if(i!=y and (tablero[0][x][i] == 1)):
            conteo += 1
        i += 1
    
    i = 0
    while(i>=0 and i<N):
        if(i!=x and (tablero[0][i][y] == 1)):
            conteo += 1
        i += 1
    
    i = x-1; j = y-1
    while(i>=0 and j>=0):
        if(tablero[0][i][j] == 1):
            conteo += 1
        i-=1; j-=1
    
    i = x+1; j = y-1
    while(i<N and j>=0):
        if(tablero[0][i][j] == 1):
            conteo += 1
        i+=1; j-=1
    
    i = x-1; j = y+1
    while(i>=0 and j<N):
        if(tablero[0][i][j] == 1):
            conteo += 1
        i-=1; j+=1
    
    i = x+1; j = y+1
    while(i<N and j<N):
        if(tablero[0][i][j] == 1):
            conteo += 1
        i+=1; j+=1
    
    return conteo

def hay_conflicto(N, tablero, x, y):
    i = 0
    while(i<N):
        if(i!=y and (tablero[0][x][i] == 1)):
            return True
        i += 1
    
    i = 0
    while(i<N):
        if(i!=x and (tablero[0][i][y] == 1)):
            return True
        i += 1
    
    i = x-1; j = y-1
    while(i>=0 and j>=0):
        if(tablero[0][i][j] == 1):
            return True
        i-=1; j-=1
    
    i = x+1; j = y-1
    while(i<N and j>=0):
        if(tablero[0][i][j] == 1):
            return True
        i+=1; j-=1
    
    i = x-1; j = y+1
    while(i>=0 and j<N):
        if(tablero[0][i][j] == 1):
            return True
        i-=1; j+=1
    
    i = x+1; j = y+1
    while(i<N and j<N):
        if(tablero[0][i][j] == 1):
            return True
        i+=1; j+=1
    
    return False

def print_tablero(N, tablero):
    i = 0
    cadena = "\033[38;2;127;48;0m"
    while(i<(N+2)):
        cadena += "██"; i+=1
    cadena += "\033[0m"
    print(cadena)
    
    i = 0
    while(i < N):
        j = 0
        cadena = "\033[38;2;127;48;0m██\033[31m"
        while(j < N):
            if(i%2 == j%2):
                cadena+="\033[40m"
            else:
                cadena+="\033[47m"
            if(tablero[0][i][j] == 1):
                cadena += " R"
            else:
                cadena += "  "
            """elif(tablero[0][i][j] == -1):
                cadena += "-1" """
            j+=1
        cadena += "\033[38;2;127;48;0m██\033[0m"
        print(cadena)
        i+=1

    i = 0
    cadena = "\033[38;2;127;48;0m"
    while(i<(N+2)):
        cadena += "██"; i+=1
    cadena += "\033[0m"
    print(cadena)
    print("\033[0m")

def N_reinas(N):
    if(N == 2 or N == 3):
        return None
    intentos = 1

    while(True):
        # Nuevo intento
        tablero = [[[0] * N for _ in range(N)], True]
        for filas in tablero[0]:
            x = randint(0, N-1)
            filas[x] = 1
        print("\033[93mNuevo inicio:")
        print_tablero(N, tablero)

        contador_movimientos = 0
        while(True):
            # Buscar las reinas con más conflictos
            reinas_mayores = []
            i=0;
            while(i < N):
                j=0
                while(j<N):
                    if(tablero[0][i][j] == 1):
                        conflictos = contar_conflictos(N, tablero, i, j)
                        if(len(reinas_mayores) == 0):
                            objeto = [i, j, conflictos]
                            reinas_mayores.append(objeto)
                        else:
                            if(conflictos == reinas_mayores[-1][2]):
                                objeto = [i, j, conflictos]
                                reinas_mayores.append(objeto)
                            elif(conflictos > reinas_mayores[-1][2]):
                                reinas_mayores = []
                                objeto = [i, j, conflictos]
                                reinas_mayores.append(objeto)
                    j+=1
                i+=1
            
            if(debug): print("\033[94mReinas con más conflictos: \033[0m")
            cadena = ""
            i=0
            while(i<len(reinas_mayores)):
                cadena += "("+str(reinas_mayores[i][0]) + ", " + str(reinas_mayores[i][1]) + ")"
                i += 1
            if(debug): print(cadena)
            if(debug): print("Con \033[94m" + str(reinas_mayores[0][2]) + " \033[0mconflictos.")
            
            # Seleccionar alguna de las reinas con más conflictos
            n = randint(0, len(reinas_mayores)-1)
            fila_seleccionada = reinas_mayores[n][0]
            col_seleccionada = reinas_mayores[n][1]
            if(debug): print("\033[94m\nQuitamos la reina en:\033[0m ("+ str(fila_seleccionada) +", " + str(col_seleccionada) +")\033[0m")
            tablero[0][fila_seleccionada][col_seleccionada] = 0

            # Mover de lugar a posición con menos conflictos
            casillas = []
            i = 0
            while(i < N):
                conflictos = contar_conflictos(N, tablero, fila_seleccionada, i)
                if(len(casillas) == 0):
                    objeto = [fila_seleccionada, i, conflictos]
                    casillas.append(objeto)
                else:
                    if(conflictos == casillas[-1][2]):
                        objeto = [fila_seleccionada, i, conflictos]
                        casillas.append(objeto)
                    elif(conflictos < casillas[-1][2]):
                        casillas = []
                        objeto = [fila_seleccionada, i, conflictos]
                        casillas.append(objeto)
                i += 1
            
            if(debug): print("\033[94m\nCasillas con menos conflictos: \033[0m")
            cadena = ""
            i = 0
            while(i<len(casillas)):
                cadena += "("+str(casillas[i][0]) + ", " + str(casillas[i][1]) + ")"
                i += 1
            if(debug): print(cadena)
            if(debug): print("Con \033[94m" + str(casillas[0][2]) + " \033[0mconflictos.")

            # Seleccionar alguna de las casillas con menos conflictos
            n = randint(0, len(casillas)-1)
            col_seleccionada = casillas[n][1]
            if(debug): print("\033[94m\nColocamos la reina en:\033[0m ("+ str(fila_seleccionada) +", " + str(col_seleccionada) +")\033[0m")
            tablero[0][fila_seleccionada][col_seleccionada] = 1
            contador_movimientos += 1
            

            if(debug): print("\033[92mResultado: \033[0m")
            if(debug): print_tablero(N, tablero)
            
            # Buscar si conflictos
            i = 0
            correcto = True
            while(i < N):
                j = 0
                while(j < N):
                    if(tablero[0][i][j] == 1):
                        if(hay_conflicto(N, tablero, i, j)):
                            correcto = False
                            j = N; i = N
                    j += 1
                i += 1
            if(correcto): 
                print("\033[93mCORRECTO\033[0m")
                print_tablero(N, tablero)
                print("\033[92mTomó \033[0m" + str(intentos) + " \033[92mtableros iniciales")
                print("\033[92mTomó \033[0m" + str(contador_movimientos) + " \033[92mmovimientos llegar a la solución desde el tablero inicial.\033[0m")
                return tablero
            else:
                if(contador_movimientos > 1000):
                    intentos += 1
                    print("\033[31mSe hicieron más de 1000 movimientos sin llegar a una solución. Reiniciamos todo el tablero.\033[0m")
                    break