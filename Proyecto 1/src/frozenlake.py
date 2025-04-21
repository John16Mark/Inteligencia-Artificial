import gymnasium as gym
from gymnasium.envs.toy_text.frozen_lake import generate_random_map
import pygame

#######################################################################
#                         FUNCIONES GENERALES
#######################################################################

mapa_personalizado = [
    "SFFFF",
    "FHFFH",
    "FFFFF",
    "HFFHF",
    "GFFFF"
]

# 0 -> Default
# 1 -> Personalizado
# 2 -> Aleatorio
tipo_mapa = 1

def construir_grafo(matriz):
    grafo = {}
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            objeto = (i, j)
            adyacentes = {}
            if(i-1 >= 0 and matriz[i-1][j] != b'H'): # Arriba
                adyacentes.update({(i-1, j): 1})
            if(j+1 < len(matriz) and matriz[i][j+1] != b'H'): # Derecha
                adyacentes.update({(i, j+1): 1})
            if(i+1 < len(matriz) and matriz[i+1][j] != b'H'): # Abajo
                adyacentes.update({(i+1, j): 1})
            if(j-1 >= 0 and matriz[i][j-1] != b'H'): # Izquierda
                adyacentes.update({(i, j-1): 1})
            grafo.update({objeto: adyacentes})
    return grafo

def obtener_inicial_y_final(matriz):
    inicial = None
    final = None
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == b'S':
                inicial = (i, j)
            elif matriz[i][j] == b'G':
                final = (i, j)
    return inicial, final

def obtener_movimiento(antes, despues):
    dx = despues[0] - antes[0]
    dy = despues[1] - antes[1]
    if dx == -1: return 3  # arriba
    if dx == 1: return 1   # abajo
    if dy == -1: return 0  # izquierda
    if dy == 1: return 2   # derecha

#######################################################################
#                         BREADTH FIRST SEARCH
#######################################################################

def BFS_rec(grafo, actual, final, cola, visitados, previos):
    cola.pop(0)
    visitados.append(actual)
    if(actual == final):
        print("\033[94mSe encontró el oro en ", actual, "\033[0m")
        return True
    print("\033[92mVisitamos ", actual, "\033[0m")
    adyacentes = grafo.get(actual)
    for casilla in adyacentes:
        if casilla not in visitados and casilla not in cola:
            print("\033[93mEncolamos ", casilla, "\033[0m")
            cola.append(casilla)
            previos.update({ casilla: actual})
        else:
            print("\033[91mYa visitamos ", casilla, " anteriormente\033[0m")
    if(len(cola) == 0):
        return False
    nuevo = cola[0]
    encontrado = BFS_rec(grafo, nuevo, final, cola, visitados, previos)
    if(encontrado == True):
        return True
    print("\033[96mRegresamos de ", nuevo, "\033[0m")
    return False

def BFS(matriz):
    grafo = construir_grafo(matriz)
    inicial, final = obtener_inicial_y_final(matriz)
    print("\033[93mInicial: \033[0m", inicial)
    print("\033[93mFinal: \033[0m", final)

    cola = []
    visitados = []
    previos = { inicial: None }
    cola.append(inicial)
    resultado = BFS_rec(grafo, inicial, final, cola, visitados, previos)
    if(resultado == True):
        ruta = []
        ruta.append(final)
        siguiente = previos.get(final)
        while(siguiente != None):
            ruta.insert(0, siguiente)
            siguiente = previos.get(siguiente)
        return ruta
    else:
        return None

def fl_BFS():
    if(tipo_mapa == 0):
        env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="human")
    elif(tipo_mapa == 1):
        env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="human", desc=mapa_personalizado)
    else:
        random_map = generate_random_map(size=6, p=0.9)
        env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="human", desc=random_map)
    matriz = env.unwrapped.desc
    
    ruta = BFS(matriz)
    if(ruta == None):
        print("\033[31mNo se encontró el oro\033[0m")
    else:
        print("\n\033[95mRuta: \033[0m", ruta)
    
    obs, info = env.reset()
    for i in range(len(ruta)-1):
        antes = ruta[i]
        depues = ruta[i+1]
        accion = obtener_movimiento(antes, depues)
        obs, reward, done, truncated, info = env.step(accion)
        env.render()
        if done:
            break
    env.close()

#######################################################################
#                           DEPTH FIRST SEARCH
#######################################################################

def DFS_rec(grafo, actual, final, pila, visitados):
    if(actual == final):
        print("\033[94mSe encontró el oro en ", actual, "\033[0m")
        return True
    adyacentes = grafo.get(actual)
    for casilla in adyacentes: 
        pila.append(casilla)
        encontrado = False
        if casilla not in visitados:
            print("\033[92mBuscamos en ", casilla, "\033[0m")
            visitados.append(casilla)
            encontrado = DFS_rec(grafo, casilla, final, pila, visitados)
            if(encontrado == True):
                return True
            print("\033[93mRegresamos de ", casilla, "\033[0m")
        else:
            print("\033[91mYa visitamos ", casilla, " anteriormente\033[0m")
        pila.pop()
    return False

def DFS(matriz):
    grafo = construir_grafo(matriz)
    inicial, final = obtener_inicial_y_final(matriz)
    print("\033[93mInicial: \033[0m", inicial)
    print("\033[93mFinal: \033[0m", final)

    pila = []
    visitados = []
    pila.append(inicial)
    resultado = DFS_rec(grafo, inicial, final, pila, visitados)
    if(resultado == True):
        return pila
    else:
        return None

def fl_DFS():
    if(tipo_mapa == 0):
        env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="human")
    elif(tipo_mapa == 1):
        env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="human", desc=mapa_personalizado)
    else:
        random_map = generate_random_map(size=6, p=0.9)
        env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="human", desc=random_map)
    matriz = env.unwrapped.desc
    
    ruta = DFS(matriz)
    if(ruta == None):
        print("\033[31mNo se encontró el oro\033[0m")
    else:
        print("\n\033[95mRuta: \033[0m", ruta)
    
    obs, info = env.reset()
    for i in range(len(ruta)-1):
        antes = ruta[i]
        depues = ruta[i+1]
        accion = obtener_movimiento(antes, depues)
        obs, reward, done, truncated, info = env.step(accion)
        env.render()
        if done:
            break
    env.close()