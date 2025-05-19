from lib.consola import gotoxy, enable_ansi_escape, clrscr
from lib.diseno import print_letra, colorDefault, customForeground
from lib.menus import menu_principal, titulo_BFS, titulo_DFS, titulo_greedy, titulo_A, titulo_hill_climbing, titulo_minimax

from src.rumania import esta_ciudad, BFS, DFS, greedy, A_estrella, hill_climbing
from src.frozenlake import fl_BFS, fl_DFS, fl_A
from src.reinas import N_reinas
from src.gato import partida_3_raya

# Activar soporte ANSI (solo necesario en Windows)
enable_ansi_escape()

def menu_BFS():
    opcion = 0
    while(opcion != 3):
        clrscr()
        titulo_BFS()
        print("\n   Seleccionar el entorno.\n")
        print("  1.- Frozen Lake")
        print("  2.- Mapa de Rumania")
        print("  3.- Salir")
        opcion = int(input("\n   Seleccione la opción deseada: "))

        # Frozen Lake
        if(opcion == 1):
            clrscr()
            titulo_BFS()
            fl_BFS()
            customForeground(255,135,191)
            input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")
        # Mapa de Rumania
        elif (opcion == 2):
            clrscr()
            titulo_BFS()
            print("\n   Seleccionar las ciudades.\n")
            inicial = input("\n   \033[93mCiudad de origen: \033[0m")
            # Si no existe la ciudad introducida
            if(esta_ciudad(inicial) == False):
                print("\033[91m\n   La ciudad ", inicial, " no se encuentra en el mapa.\033[0m")
                customForeground(255,135,191)
                input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")
            else:
                final = input("   \033[93mCiudad destino: \033[0m")
                # Si no existe la ciudad introducida
                if(esta_ciudad(final) == False):
                    print("\033[91m\n   La ciudad ", final, " no se encuentra en el mapa.\033[0m")
                    customForeground(255,135,191)
                    input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")
                else:
                    clrscr()
                    titulo_BFS()  
                    ruta = BFS(inicial.title(), final.title())
                    if(ruta == None):
                        print("\033[31mNo se encontró la ciudad ", final, "\033[0m")
                    else:
                        print("\n\033[95mRuta: \033[0m", ruta)
                    customForeground(255,135,191)
                    input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")

def menu_DFS():
    opcion = 0
    while(opcion != 3):
        clrscr()
        titulo_DFS()
        print("\n   Seleccionar el entorno.\n")
        print("  1.- Frozen Lake")
        print("  2.- Mapa de Rumania")
        print("  3.- Salir")
        opcion = int(input("\n   Seleccione la opción deseada: "))

        # Frozen Lake
        if(opcion == 1):
            clrscr()
            titulo_DFS()
            fl_DFS()
            customForeground(255,135,191)
            input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")
        # Mapa de Rumania
        elif (opcion == 2):
            clrscr()
            titulo_DFS()
            print("\n   Seleccionar las ciudades.\n")
            inicial = input("\n   \033[93mCiudad de origen: \033[0m")
            # Si no existe la ciudad introducida
            if(esta_ciudad(inicial) == False):
                print("\033[91m\n   La ciudad ", inicial, " no se encuentra en el mapa.\033[0m")
                customForeground(255,135,191)
                input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")
            else:
                final = input("   \033[93mCiudad destino: \033[0m")
                # Si no existe la ciudad introducida
                if(esta_ciudad(final) == False):
                    print("\033[91m\n   La ciudad ", final, " no se encuentra en el mapa.\033[0m")
                    customForeground(255,135,191)
                    input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")
                else:
                    clrscr()
                    titulo_DFS()  
                    ruta = DFS(inicial.title(), final.title())
                    if(ruta == None):
                        print("\033[31mNo se encontró la ciudad ", final, "\033[0m")
                    else:
                        print("\n\033[95mRuta: \033[0m", ruta)
                    customForeground(255,135,191)
                    input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")

def menu_greedy():
    opcion = 0
    while(opcion != 2):
        clrscr()
        titulo_greedy()
        print("\n   Seleccionar el entorno.\n")
        print("  1.- Mapa de Rumania")
        print("  2.- Salir")
        opcion = int(input("\n   Seleccione la opción deseada: "))
        
        # Mapa de Rumania
        if (opcion == 1):
            clrscr()
            titulo_greedy()
            print("\n   Seleccionar las ciudades.\n")
            inicial = input("\n   \033[93mCiudad de origen: \033[0m")
            inicial = inicial.title()
            # Si no existe la ciudad introducida
            if(esta_ciudad(inicial) == False):
                print("\033[91m\n   La ciudad ", inicial, " no se encuentra en el mapa.\033[0m")
                customForeground(255,135,191)
                input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")
            else:
                final = input("   \033[93mCiudad destino: \033[0m")
                final = final.title()
                # Si no existe la ciudad introducida
                if(esta_ciudad(final) == False):
                    print("\033[91m\n   La ciudad ", final, " no se encuentra en el mapa.\033[0m")
                    customForeground(255,135,191)
                    input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")
                else:
                    clrscr()
                    titulo_greedy()  
                    ruta, distancia = greedy(inicial, final)
                    if(ruta == None):
                        print("\033[31mNo se llegó a la ciudad ", final, "\033[0m")
                    else:
                        print("\n\033[95mRuta: \033[0m", ruta)
                        print("\033[95mDistancia recorrida: \033[0m", distancia)
                    customForeground(255,135,191)
                    input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")

def menu_A():
    opcion = 0
    while(opcion != 3):
        clrscr()
        titulo_A()
        print("\n   Seleccionar el entorno.\n")
        print("  1.- Frozen Lake")
        print("  2.- Mapa de Rumania")
        print("  3.- Salir")
        opcion = int(input("\n   Seleccione la opción deseada: "))

        # Frozen Lake
        if (opcion == 1):
            clrscr()
            titulo_A()
            fl_A()
            customForeground(255,135,191)
            input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")
        # Mapa de Rumania  
        elif(opcion == 2):
            clrscr()
            titulo_A()
            print("\n   \033[93mCiudad de origen: \033[0mArad")
            print("   \033[93mCiudad destino: \033[0mBucharest")
            ruta, distancia = A_estrella("Arad", "Bucharest")
            if(ruta == None):
                print("\033[31mNo se llegó a Bucharest\033[0m")
            else:
                print("\n\033[95mRuta: \033[0m", ruta)
                print("\033[95mDistancia recorrida: \033[0m", distancia)
            customForeground(255,135,191)
            input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")

def menu_hill_c():
    opcion = 0
    while(opcion != 3):
        clrscr()
        titulo_hill_climbing()
        print("\n   Seleccionar el entorno.\n")
        print("  1.- Mapa de Rumania")
        print("  2.- Las N Reinas")
        print("  3.- Salir")
        opcion = int(input("\n   Seleccione la opción deseada: "))
        #opcion = 1
        if(opcion == 1):
            clrscr()
            titulo_hill_climbing()
            print("\n   Seleccionar las ciudades.\n")
            inicial = input("\n   \033[93mCiudad de origen: \033[0m")
            #inicial = "Bucharest"
            inicial = inicial.title()
            # Si no existe la ciudad introducida
            if(esta_ciudad(inicial) == False):
                print("\033[91m\n   La ciudad ", inicial, " no se encuentra en el mapa.\033[0m")
                customForeground(255,135,191)
                input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")
            else:
                final = input("   \033[93mCiudad destino: \033[0m")
                #final = "Arad"
                final = final.title()
                # Si no existe la ciudad introducida
                if(esta_ciudad(final) == False):
                    print("\033[91m\n   La ciudad ", final, " no se encuentra en el mapa.\033[0m")
                    customForeground(255,135,191)
                    input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")
                else:
                    clrscr()
                    titulo_hill_climbing()  
                    ruta, distancia = hill_climbing(inicial, final)
                    if(ruta == None):
                        print("\033[31mNo se llegó a la ciudad ", final, "\033[0m")
                    else:
                        print("\n\033[95mRuta: \033[0m", ruta)
                        print("\033[95mDistancia recorrida: \033[0m", distancia)
                    customForeground(255,135,191)
                    input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")
        elif(opcion == 2):
            clrscr()
            titulo_hill_climbing()
            print("\n   Seleccionar el tamaño del tablero.\n")
            tam = int(input("\n   \033[93mTamaño: \033[0m"))

            resultado = N_reinas(tam)
            if(resultado == None):
                print("\033[31mNo se puede llegar a una solución\033[0m")
            customForeground(255,135,191)
            input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")


def menu_minimax():
    opcion = 0
    while(opcion != 2):
        clrscr()
        titulo_minimax()
        print("\n   Seleccionar el entorno.\n")
        print("  1.- Tres en raya")
        print("  2.- Salir")
        opcion = int(input("\n   Seleccione la opción deseada: "))
        if(opcion == 1):
            opcion2 = 0
            while(opcion2 != 3):
                clrscr()
                titulo_minimax()
                print("\n   Seleccionar el modo de juego.\n")
                print("  1.- CPU invencible")
                print("  2.- CPU que no gana")
                print("  3.- Salir")
                opcion2 = int(input("\n   Seleccione la opción deseada: "))
                if(opcion2 == 1):
                    imbatible = True
                elif(opcion2 == 2):
                    imbatible = False
                if(opcion2 == 1 or opcion2 == 2):
                    clrscr()
                    titulo_minimax()
                    partida_3_raya(imbatible, 55, 9)
                    customForeground(255,135,191)
                    input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")

opcion = 0
while(opcion != 7):
    clrscr()
    menu_principal()
    opcion = int(input("\n   Seleccione la opción deseada: "))
    #opcion = 5
    if(opcion == 1):
        menu_BFS()
    elif(opcion == 2):
        menu_DFS()
    elif(opcion == 3):
        menu_greedy()
    elif(opcion == 4):
        menu_A()
    elif(opcion == 5):
        menu_hill_c()
    elif(opcion == 6):
        menu_minimax()
    elif(opcion == 7):
        exit(0)

