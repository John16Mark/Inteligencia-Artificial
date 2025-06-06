import heapq

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

############################# DFS

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

def Dijkstra(inicial, final):
    cola = []
    visitados = [inicial]
    previos = { inicial: None }
    cola.append((0, inicial))
    resultado = Dijkstra_rec((0, inicial), final, cola, visitados, previos, 0)
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

def Dijkstra_rec(actual, final, cola, visitados, previos, distancia):
    cola.pop(0)
    visitados.append(actual)
    if(actual[1] == final):
        print("\033[94mSe encontró ", actual[1], "\033[0m")
        return True
    print("\033[92mVisitamos ", actual[1], "\033[0m")
    adyacentes = grafo.get(actual[1])
    print(adyacentes)
    
    for ciudad in adyacentes:
        # Si no hemos visitado ya la ciudad
        if ciudad not in visitados:
            # Si no está ya en las ciudades por visitar, añadimos
            dist_acum = distancia + adyacentes[ciudad]
            if ciudad not in [ciud for _, ciud in cola]:
                print("\033[93mEncolamos ", ciudad, "\033[0m")
                heapq.heappush(cola, (dist_acum, ciudad))
                previos.update({ciudad: actual[1]})
            # Si está en las ciudades por visitar, comprobamos si la distancia es mejor
            else:
                print("\033[38;2;255;144;0mYa tenemos encolada ", ciudad, "\033[0m")
                
                for i, (dist, c) in enumerate(cola):
                    if c == ciudad:
                        if dist_acum < dist:
                            print("\033[32mMejor distancia para, ", ciudad, " desde ", actual[1], " - ", dist_acum, " < ", dist, "\033[0m")
                            del cola[i]
                            heapq.heapify(cola)
                            heapq.heappush(cola, (dist_acum, ciudad))
                            previos[ciudad] = actual[1]
                        else:
                            print("\033[31mLa distancia es peor: ", dist_acum, " > ", dist)
        else:
            print("\033[91mYa visitamos ", ciudad, " anteriormente\033[0m")
    if(len(cola) == 0):
        return False
    for e in cola:
        print("\033[96m ", e[1], ": ", e[0], "\033[0m")
    nuevo = cola[0]
    visitados.append(nuevo[1])
    print("Nuevo: ", nuevo)
    print("Nuevo[0]: ", nuevo[0])
    encontrado = Dijkstra_rec(nuevo, final, cola, visitados, previos, nuevo[0])
    if(encontrado == True):
        return True
    print("\033[96mRegresamos de ", nuevo, "\033[0m")
    return False

inicial = "Arad"
final = "Bucharest"
"""
print("\n\033[95m -- Depth First Search --\033[0m")     
ruta = DFS(inicial, final)
if(ruta == None):
    print("\033[31mNo se encontró la ciudad ", final, "\033[0m")
else:
    print("Ruta: ", ruta)

print("\n\033[95m -- Breadth First Search --\033[0m")    
ruta = BFS(inicial, final)
if(ruta == None):
    print("\033[31mNo se encontró la ciudad ", final, "\033[0m")
else:
    print("Ruta: ", ruta)
"""
print("\n\033[95m -- Dijkstra's --\033[0m")    
ruta = Dijkstra(inicial, final)
if(ruta == None):
    print("\033[31mNo se encontró la ciudad ", final, "\033[0m")
else:
    print("Ruta: ", ruta)