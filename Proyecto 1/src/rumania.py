import heapq
from random import randint
import random

# Grafo representado con un diccionario
grafo = {
    "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Sibiu": {"Oradea": 151, "Arad": 140, "Fagaras": 99, "Rimnicu Vilcea": 80},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70},
    "Mehadia": {"Lugoj": 70, "Drobeta": 75},
    "Drobeta": {"Craiova": 120, "Mehadia": 75},
    "Fagaras": {"Sibiu": 99, "Bucharest": 211},
    "Rimnicu Vilcea": {"Sibiu": 80, "Pitesti": 97, "Craiova": 146},
    "Craiova": {"Drobeta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
    "Pitesti": {"Craiova": 138, "Rimnicu Vilcea": 97, "Bucharest": 101},
    "Bucharest": {"Fagaras": 211, "Pitesti": 101, "Giurgui": 90, "Urziceni": 85},
    "Urziceni": {"Bucharest": 85, "Vaslui": 142, "Hirsova": 98},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Vaslui": {"Urziceni": 142, "Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Giurgui": {"Bucharest": 90},
    "Neamt": {"Iasi": 87},
    "Eforie": {"Hirsova": 86},
}

heuristica = {
    "Arad": 366,
    "Zerind": 374,
    "Oradea": 380,
    "Sibiu": 253,
    "Timisoara": 329,
    "Lugoj": 244,
    "Mehadia": 241,
    "Drobeta": 242,
    "Fagaras": 176,
    "Rimnicu Vilcea": 193, 
    "Craiova": 160,
    "Pitesti": 100,
    "Bucharest": 0,
    "Urziceni": 80,
    "Hirsova": 151,
    "Vaslui": 199,
    "Iasi": 226,
    "Giurgui": 77,
    "Neamt": 234,
    "Eforie": 161,
}

def esta_ciudad(ciudad):
    return grafo.get(ciudad.title()) != None

#######################################################################
#                           DEPTH FIRST SEARCH
#######################################################################

def DFS_rec(actual, final, pila, visitados):
    if(actual == final):
        print("\033[94mSe encontró ", actual, "\033[0m")
        return True
    adyacentes = grafo.get(actual)
    for ciudad in adyacentes: 
        pila.append(ciudad)
        encontrado = False
        if ciudad not in visitados:
            print("\033[92mBuscamos en ", ciudad, "\033[0m")
            visitados.append(ciudad)
            encontrado = DFS_rec(ciudad, final, pila, visitados)
            if(encontrado == True):
                return True
            print("\033[93mRegresamos de ", ciudad, "\033[0m")
        else:
            print("\033[91mYa visitamos ", ciudad, " anteriormente\033[0m")
        pila.pop()
    return False

def DFS(inicial, final):
    pila = []
    visitados = []
    pila.append(inicial)
    visitados.append(inicial)
    resultado = DFS_rec(inicial, final, pila, visitados)
    if(resultado == True):
        return pila
    else:
        return None

#######################################################################
#                         BREADTH FIRST SEARCH
#######################################################################

def BFS_rec(actual, final, cola, visitados, previos):
    cola.pop(0)
    visitados.append(actual)
    if(actual == final):
        print("\033[94mSe encontró ", actual, "\033[0m")
        return True
    print("\033[92mVisitamos ", actual, "\033[0m")
    adyacentes = grafo.get(actual)
    for ciudad in adyacentes:
        if ciudad not in visitados and ciudad not in cola:
            print("\033[93mEncolamos ", ciudad, "\033[0m")
            cola.append(ciudad)
            previos.update({ ciudad: actual})
        else:
            print("\033[91mYa visitamos ", ciudad, " anteriormente\033[0m")
    if(len(cola) == 0):
        return False
    nuevo = cola[0]
    encontrado = BFS_rec(nuevo, final, cola, visitados, previos)
    if(encontrado == True):
        return True
    print("\033[96mRegresamos de ", nuevo, "\033[0m")
    return False

def BFS(inicial, final):
    cola = []
    visitados = []
    previos = { inicial: None }
    cola.append(inicial)
    resultado = BFS_rec(inicial, final, cola, visitados, previos)
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

#######################################################################
#                          ALGORITMO GREEDY
#######################################################################

def greedy(inicial, final):
    ruta = [inicial]
    actual = inicial
    distancia = 0
    while(actual != final):
        print("\033[92mVisitamos ", actual, "\033[0m")
        adyacentes = grafo.get(actual)
        mejor = None
        for ciudad in adyacentes:
            if ciudad not in ruta:
                print("\033[93mNo hemos visitado ", ciudad, " anteriormente\033[0m")
                if(mejor == None or adyacentes[ciudad] < mejor[1]):
                    mejor = (ciudad, adyacentes[ciudad])
            else:
                print("\033[91mYa visitamos ", ciudad, " anteriormente\033[0m")
        if(mejor == None):
            return None, None
        actual = mejor[0]
        distancia += mejor[1]
        ruta.append(actual)
    print("\033[94mSe encontró ", final, "\033[0m")
    return ruta, distancia

#######################################################################
#                              ALGORITMO A*
#######################################################################

def A_rec(actual, final, cola, visitados, previos):
    #cola.pop(0)
    visitados.append(actual)
    if(actual[1] == final):
        print("\033[94mSe encontró ", actual[1], "\033[0m")
        return True
    print("\033[92mVisitamos ", actual[1], "\033[0m")
    adyacentes = grafo.get(actual[1])
    
    for ciudad in adyacentes:
        # Si no hemos visitado ya la ciudad
        if ciudad not in visitados:
            # Si no está ya en las ciudades por visitar, añadimos
            if ciudad not in [ciud for _, ciud in cola]:
                print("\033[93mEncolamos ", ciudad, " - g(x)=", adyacentes[ciudad], " + h(x)=", heuristica[ciudad], ": ", adyacentes[ciudad] + heuristica[ciudad],"\033[0m")
                heapq.heappush(cola, (adyacentes[ciudad] + heuristica[ciudad], ciudad))
                previos.update({ciudad: actual[1]})
            # Si está en las ciudades por visitar, comprobamos si la distancia es mejor
            else:
                print("\033[38;2;255;144;0mYa tenemos encolada ", ciudad, "\033[0m")
                
                for i, (dist_temporal, ciudad_temporal) in enumerate(cola):
                    if ciudad_temporal == ciudad:
                        if adyacentes[ciudad] + heuristica[ciudad] < dist_temporal + heuristica[ciudad_temporal]:
                            print("\033[32mMejor distancia para, ", ciudad, " desde ", actual[1], " - g(x)=", adyacentes[ciudad], " + h(x)=", heuristica[ciudad]," < ", dist_temporal + heuristica[ciudad_temporal], "\033[0m")
                            del cola[i]
                            heapq.heapify(cola)
                            heapq.heappush(cola, (adyacentes[ciudad] + heuristica[ciudad], ciudad))
                            previos[ciudad] = actual[1]
                        else:
                            print("\033[31mLa distancia es peor: - g(x)=", adyacentes[ciudad], " + h(x)=", heuristica[ciudad]," > ", dist_temporal + heuristica[ciudad_temporal])
        else:
            print("\033[91mYa visitamos ", ciudad, " anteriormente\033[0m")
    if(len(cola) == 0):
        return False

    nuevo = heapq.heappop(cola)
    visitados.append(nuevo[1])
    encontrado = A_rec(nuevo, final, cola, visitados, previos)
    if(encontrado == True):
        return True
    print("\033[96mRegresamos de ", nuevo, "\033[0m")
    return False

def A_estrella(inicial, final):
    cola = []
    visitados = [inicial]
    previos = { inicial: None }
    #cola.append((0, inicial))
    resultado = A_rec((0, inicial), final, cola, visitados, previos)
    if(resultado == True):
        distancia = 0
        ruta = []
        ruta.append(final)
        siguiente = previos.get(final)
        if(siguiente != None):
            distancia += grafo[siguiente][final]
        while(siguiente != None):
            ruta.insert(0, siguiente)
            anterior = siguiente
            siguiente = previos.get(siguiente)
            if(siguiente != None):
                distancia += grafo[siguiente][anterior]
        return ruta, distancia
    else:
        return None, None

#######################################################################
#                            HILL-CLIMBING
#######################################################################

def hc_rec(actual, final, cola):
    cola.append(actual)
    print("\033[92mVisitamos ", actual, "\033[0m")
    if(actual == final):
        print("\033[94mSe encontró ", actual, "\033[0m")
        return True
    adyacentes = grafo.get(actual)
    mejor = None
    for ciudad in adyacentes:
        if ciudad not in cola:
            print("\033[93m", ciudad, " no está encolada\033[0m")
            if(mejor == None or adyacentes[ciudad] < mejor[1]):
                mejor = (ciudad, adyacentes[ciudad])
        else:
            print("\033[91mYa visitamos ", ciudad, " anteriormente\033[0m")
    if(mejor == None):
        return False
    print("\033[33mCiudad más cercana: ", mejor[0], "\033[0m")
    encontrado = hc_rec(mejor[0], final, cola)

def hill_climbing(inicial, final):
    cola = [inicial]
    actual = inicial
    intentos = 0
    while(actual != final and intentos < 1000):
        # Fase de seguir con la ruta
        print("\033[92mVisitamos ", actual, "\033[0m")
        adyacentes = grafo.get(actual)
        mejor = None
        for ciudad in adyacentes:
            if ciudad not in cola:
                print("\033[93m", ciudad, " no está encolada\033[0m")
                if(mejor == None or adyacentes[ciudad] < mejor[1]):
                    mejor = (ciudad, adyacentes[ciudad])
            else:
                print("\033[91mYa visitamos ", ciudad, " anteriormente\033[0m")
        if(mejor != None):
            actual = mejor[0]
            cola.append(actual)
        else:
            # Fase de reseteo aleatorio
            print("\033[91mEstamos atorados en: ", cola, "\033[0m")
            intentos += 1
            nuevo = None
            while(nuevo == None):
                if(len(cola)-2 == 0):
                    indice = 0
                else:
                    indice = randint(0, len(cola)-2)
                ciudad_de_reseteo = cola[indice]
                ciudades = grafo.get(ciudad_de_reseteo)
                
                bloqueada = cola[indice+1]
                ciudades_disponibles = [ciudad for ciudad in ciudades if ciudad != bloqueada and ciudad not in cola]
                if(len(ciudades_disponibles) == 0):
                    print("\033[91mNo se puede reiniciar desde ", ciudad_de_reseteo, "\033[0m")
                    continue
                actual = random.choice(ciudades_disponibles)
                primera_mitad = cola[:indice+1]
                cola = primera_mitad
                cola.append(actual)
                print("Reseteamos desde ", actual)
                print("Nueva cola: ", cola)
                break
                


    if(intentos >= 1000):
        return None, None
    else:
        
        distancia = 0
        indice = 0
        actual = cola[indice]
        while(actual != final): 
            ciudades = grafo.get(actual)
            indice += 1
            distancia += ciudades.get(cola[indice])
            actual = cola[indice]
        print(distancia)
        return cola, distancia