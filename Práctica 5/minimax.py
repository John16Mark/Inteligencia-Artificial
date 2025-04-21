import math

valores = [3, 5, 6, 9, 1, 2, 0, -1]
profundidad_maxima = int(math.log2(len(valores)))
print("\033[92mProfundidad máxima del árbol: \033[0m", profundidad_maxima)

evaluaciones_sin_poda = 0
evaluaciones_con_poda = 0

def minimax(indice, profundidad, maximiza):
    print("Evaluamos nodo \033[94míndice: \033[0m", indice, " \033[94mprofundidad: \033[0m", profundidad)
    global evaluaciones_sin_poda
    evaluaciones_sin_poda += 1
    if(profundidad == profundidad_maxima):
        return valores[indice]
    if maximiza:
        return max(
            minimax(indice*2, profundidad+1, False),
            minimax(indice*2+1, profundidad+1, False))
    else:
        return min(
            minimax(indice*2, profundidad+1, True),
            minimax(indice*2+1, profundidad+1, True))

def minimax_alphabeta(indice, profundidad, alfa, beta, maximiza):
    print("Evaluamos nodo \033[94míndice: \033[0m", indice, " \033[94mprofundidad: \033[0m", profundidad)
    global evaluaciones_con_poda
    evaluaciones_con_poda += 1
    if(profundidad == profundidad_maxima):
        return valores[indice]
    if maximiza:
        valor_max = float("-inf")
        for indice_hijo in [indice*2, indice*2+1]:
            eval = minimax_alphabeta(indice_hijo, profundidad+1, alfa, beta, False)
            valor_max = max(valor_max, eval)
            alfa = max(alfa, eval)
            if beta <= alfa: # Poda beta
                print("\033[91mHubo poda beta\033[0m")
                break
        return valor_max
    else:
        valor_min = float("inf")
        for indice_hijo in [indice*2, indice*2+1]:
            eval = minimax_alphabeta(indice_hijo, profundidad+1, alfa, beta, True)
            valor_min = min(valor_min, eval)
            beta = min(beta, eval)
            if beta <= alfa: # Poda alfa
                print("\033[91mHubo poda alfa\033[0m")
                break
        return valor_min

print("\033[95m -- Minimax --\033[0m")
resultado = minimax(0, 0, True)
print("\033[96mResultado: \033[0m", resultado)
print("\033[93mNúmero de evaluaciones: \033[0m", evaluaciones_sin_poda)

print("\033[95m -- Minimax con poda Alfa-Beta --\033[0m")
resultado = minimax_alphabeta(0, 0, float("-inf"), float("inf"), True)
print("\033[96mResultado: \033[0m", resultado)
print("\033[93mNúmero de evaluaciones: \033[0m", evaluaciones_con_poda)
