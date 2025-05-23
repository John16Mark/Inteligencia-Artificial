from .consola import gotoxy

def colorForeground(color):
    if(color == "negro"):
        print("\033[30m", end = "")
    elif (color == "rojo"): 
        print("\033[31m", end = "")
    elif (color == "verde"):
        print("\033[32m", end = "")
    elif(color == "amarillo"):
        print("\033[33m", end = "")
    elif(color == "azul"):
        print("\033[34m", end = "")
    elif(color == "magenta"):
        print("\033[35m", end = "")
    elif(color == "cian"):
        print("\033[36m", end = "")
    elif(color == "gris claro"):
        print("\033[37m", end = "")
    elif(color == "gris oscuro"):
        print("\033[90m", end = "")
    elif(color == "rojo claro"):
        print("\033[91m", end = "")
    elif(color == "verde claro"):
        print("\033[92m", end = "")
    elif(color == "amarillo claro"):
        print("\033[93m", end = "")
    elif(color == "azul claro"):
        print("\033[94m", end = "")
    elif(color == "magenta claro"):
        print("\033[95m", end = "")
    elif(color == "cian claro"):
        print("\033[96m", end = "")
    elif(color == "blanco"):
        print("\033[97m", end = "")

def colorBackground(color):
    if(color == "negro"):
        print("\033[40m", end = "")
    elif(color == "rojo"):
        print("\033[41m", end = "")
    elif(color == "verde"):
        print("\033[42m", end = "")
    elif(color == "amarillo"):
        print("\033[43m", end = "")
    elif(color == "azul"):
        print("\033[44m", end = "")
    elif(color == "magenta"):
        print("\033[45m", end = "")
    elif(color == "cian"):
        print("\033[46m", end = "")
    elif(color == "gris claro"):
        print("\033[47m", end = "")
    elif(color == "gris oscuro"):
        print("\033[100m", end = "")
    elif(color == "rojo claro"):
        print("\033[101m", end = "")
    elif(color == "verde claro"):
        print("\033[102m", end = "")
    elif(color == "amarillo claro"):
        print("\033[103m", end = "")
    elif(color == "azul claro"):
        print("\033[104m", end = "")
    elif(color == "magenta claro"):
        print("\033[105m", end = "")
    elif(color == "cian claro"):
        print("\033[106m", end = "")
    elif(color == "blanco"):
        print("\033[107m", end = "")


def customForeground(R, G, B):
    print("\033[38;2;"+str(R)+";"+str(G)+";"+str(B)+"m", end="")

def customBackground(R, G, B):
    print("\033[48;2;"+str(R)+";"+str(G)+";"+str(B)+"m", end="")

def colorDefault():
    print("\033[0m", end="")

def print_letra(letra, x, y, color1, color2, color3):
    gotoxy(x,y)
    if(letra == 'A'):
        customForeground(color1[0], color1[1], color1[2])
        print("▄▀▀▀▄")
        customBackground(color2[0], color2[1], color2[2])
        gotoxy(x, y+1)
        print("▀")
        gotoxy(x+4, y+1)
        print("▀")
        colorBackground("negro")
        customForeground(color2[0], color2[1], color2[2])
        gotoxy(x, y+2)
        print("█▀▀▀█")
        customForeground(color3[0], color3[1], color3[2])
        gotoxy(x, y+3)
        print("█   █")
        gotoxy(x, y+4)
        print("▀   ▀")
    elif(letra == 'B'):
        customForeground(color1[0], color1[1], color1[2])
        print("█▀▀▄")
        gotoxy(x, y+1)
        customBackground(color2[0], color2[1], color2[2])
        print("▀")
        gotoxy(x+3, y+1)
        print("▀")
        customForeground(color2[0], color2[1], color2[2])
        colorBackground("negro")
        gotoxy(x, y+2)
        print("█▀▀▄")
        customForeground(color3[0], color3[1], color3[2])
        gotoxy(x,y+3)
        print("█  █")
        gotoxy(x, y+4)
        print("▀▀▀")
    elif (letra == 'C'):
        customForeground(color1[0], color1[1], color1[2])
        print("▄▀▀▀")
        gotoxy(x,y+1)
        customBackground(color2[0], color2[1], color2[2])
        print("▀")
        gotoxy(x,y+2)
        print(" ")
        customForeground(color3[0], color3[1], color3[2])
        colorBackground("negro")
        gotoxy(x,y+3)
        print("█")
        gotoxy(x+1,y+4)
        print("▀▀▀")
    elif (letra == 'D'):
        customForeground(color1[0], color1[1], color1[2])
        print("█▀▀▀▄")
        gotoxy(x,y+1)
        customBackground(color2[0], color2[1], color2[2])
        print("▀")
        gotoxy(x+4,y+1)
        print("▀")
        gotoxy(x,y+2)
        print(" ")
        gotoxy(x+4,y+2)
        print(" ")
        customForeground(color3[0], color3[1], color3[2])
        colorBackground("negro")
        gotoxy(x,y+3)
        print("█")
        gotoxy(x+4,y+3)
        print("█")
        gotoxy(x,y+4)
        print("▀▀▀▀")
    elif (letra == 'E'):
        customForeground(color1[0], color1[1], color1[2])
        print("█▀▀▀")
        customBackground(color2[0], color2[1], color2[2])
        gotoxy(x,y+1)
        print("▀")
        colorBackground("negro")
        customForeground(color2[0], color2[1], color2[2])
        gotoxy(x,y+2)
        print("█▀▀")
        customForeground(color3[0], color3[1], color3[2])
        gotoxy(x,y+3)
        print("█")
        gotoxy(x,y+4)
        print("▀▀▀▀")
    elif (letra == 'F'):
        customForeground(color1[0], color1[1], color1[2])
        print("█▀▀▀")
        customBackground(color2[0], color2[1], color2[2])
        gotoxy(x,y+1)
        print("▀")
        colorBackground("negro")
        customForeground(color2[0], color2[1], color2[2])
        gotoxy(x,y+2)
        print("█▀▀")
        customForeground(color3[0], color3[1], color3[2])
        gotoxy(x,y+3)
        print("█")
        gotoxy(x,y+4)
        print("▀")
    elif (letra == 'G'):
        customForeground(color1[0], color1[1], color1[2])
        print("▄▀▀▀▄")
        gotoxy(x,y+1)
        customBackground(color2[0], color2[1], color2[2])
        print("▀")
        gotoxy(x,y+2)
        print(" ")
        colorForeground("negro")
        gotoxy(x+2,y+2)
        print("▀▀▀")
        customForeground(color3[0], color3[1], color3[2])
        colorBackground("negro")
        gotoxy(x,y+3)
        print("█   █")
        gotoxy(x+1,y+4)
        print("▀▀▀")
    elif (letra == 'H'):
        customForeground(color1[0], color1[1], color1[2])
        print("█   █")
        customBackground(color2[0], color2[1], color2[2])
        gotoxy(x,y+1)
        print("▀")
        gotoxy(x+4,y+1)
        print("▀")
        colorBackground("negro")
        customForeground(color2[0], color2[1], color2[2])
        gotoxy(x,y+2)
        print("█▀▀▀█")
        customForeground(color3[0], color3[1], color3[2])
        gotoxy(x,y+3)
        print("█   █")
        gotoxy(x,y+4)
        print("▀   ▀")
    elif (letra == 'I'):
        customForeground(color1[0], color1[1], color1[2])
        print("▀▀█▀▀")
        customBackground(color2[0], color2[1], color2[2])
        gotoxy(x+2,y+1)
        print("▀")
        gotoxy(x+2,y+2)
        print(" ")
        colorBackground("negro")
        customForeground(color3[0], color3[1], color3[2])
        gotoxy(x+2,y+3)
        print("█")
        gotoxy(x,y+4)
        print("▀▀▀▀▀")
    elif (letra == 'J'):
        customForeground(color1[0], color1[1], color1[2])
        print(" ▀▀█")
        customBackground(color2[0], color2[1], color2[2])
        gotoxy(x+3,y+1)
        print("▀")
        gotoxy(x+3,y+2)
        print(" ")
        colorBackground("negro")
        customForeground(color3[0], color3[1], color3[2])
        gotoxy(x,y+3)
        print("█  █")
        gotoxy(x,y+4)
        print(" ▀▀")
    elif (letra == 'K'):
        customForeground(color1[0], color1[1], color1[2])
        print("█  █")
        gotoxy(x+2,y+1)
        print("▀")
        customBackground(color2[0], color2[1], color2[2])
        gotoxy(x,y+1)
        print("▀")
        colorForeground("negro")
        gotoxy(x+1,y+1)
        print("▀")
        gotoxy(x, y+2)
        print(" █▄▀")
        customForeground(color3[0], color3[1], color3[2])
        colorBackground("negro")
        gotoxy(x,y+3)
        print("█  █")
        gotoxy(x,y+4)
        print("▀  ▀")
    elif (letra == 'L'):
        customForeground(color1[0], color1[1], color1[2])
        print("█")
        customBackground(color2[0], color2[1], color2[2])
        gotoxy(x,y+1)
        print("▀")
        colorBackground("negro")
        customForeground(color2[0], color2[1], color2[2])
        gotoxy(x,y+2)
        print("█")
        customForeground(color3[0], color3[1], color3[2])
        gotoxy(x,y+3)
        print("█")
        gotoxy(x,y+4)
        print("▀▀▀▀")
    elif (letra == 'M'):
        customForeground(color1[0], color1[1], color1[2])
        print("█▄   ▄█")
        gotoxy(x+2, y+1)
        print("▀ ▀")
        customBackground(color2[0], color2[1], color2[2])
        gotoxy(x,y+1)
        print("▀")
        gotoxy(x+6,y+1)
        print("▀")
        colorForeground("negro")
        gotoxy(x+3,y+1)
        print("▀")
        gotoxy(x,y+2)
        print(" █████ ")
        colorBackground("negro")
        customForeground(color3[0], color3[1], color3[2])
        gotoxy(x,y+3)
        print("█     █")
        gotoxy(x,y+4)
        print("▀     ▀")
    elif (letra == 'N'):
        customForeground(color1[0], color1[1], color1[2])
        print("█    █")
        gotoxy(x+1, y+1)
        print("▀")
        customBackground(color2[0], color2[1], color2[2])
        gotoxy(x,y+1)
        print("▀")
        gotoxy(x+5,y+1)
        print("▀")
        colorForeground("negro")
        gotoxy(x+2,y+1)
        print("▀")
        gotoxy(x,y+2)
        print(" ██▄▀ ")
        colorBackground("negro")
        customForeground(color3[0], color3[1], color3[2])
        gotoxy(x,y+3)
        print("█    █")
        gotoxy(x,y+4)
        print("▀    ▀")
    elif (letra == 'O'):
        customForeground(color1[0], color1[1], color1[2])
        print("▄▀▀▀▄")
        gotoxy(x,y+1)
        customBackground(color2[0], color2[1], color2[2])
        print("▀")
        gotoxy(x+4,y+1)
        print("▀")
        gotoxy(x,y+2)
        print(" ")
        gotoxy(x+4,y+2)
        print(" ")
        customForeground(color3[0], color3[1], color3[2])
        colorBackground("negro")
        gotoxy(x,y+3)
        print("█")
        gotoxy(x+4,y+3)
        print("█")
        gotoxy(x+1,y+4)
        print("▀▀▀")
    elif (letra == 'P'):
        customForeground(color1[0], color1[1], color1[2])
        print("█▀▀▄")
        gotoxy(x,y+1)
        customBackground(color2[0], color2[1], color2[2])
        print("▀")
        gotoxy(x+3,y+1)
        print("▀")
        gotoxy(x,y+2)
        print(" ")
        colorForeground("negro")
        gotoxy(x+1, y+2)
        print("▄▄")
        customForeground(color3[0], color3[1], color3[2])
        colorBackground("negro")
        gotoxy(x,y+3)
        print("█")
        gotoxy(x,y+4)
        print("▀")
    elif (letra == 'Q'):
        customForeground(color1[0], color1[1], color1[2])
        print("▄▀▀▀▄")
        gotoxy(x,y+1)
        customBackground(color2[0], color2[1], color2[2])
        print("▀")
        gotoxy(x+4,y+1)
        print("▀")
        gotoxy(x,y+2)
        print(" ")
        gotoxy(x+4,y+2)
        print(" ")
        customForeground(color3[0], color3[1], color3[2])
        colorBackground("negro")
        gotoxy(x,y+3)
        print("█ ▀▄█")
        gotoxy(x+1,y+4)
        print("▀▀▀▀")
    elif (letra == 'R'):
        customForeground(color1[0], color1[1], color1[2])
        print("█▀▀▄")
        gotoxy(x,y+1)
        customBackground(color2[0], color2[1], color2[2])
        print("▀")
        gotoxy(x+3,y+1)
        print("▀")
        gotoxy(x,y+2)
        print(" ")
        colorForeground("negro")
        gotoxy(x+1, y+2)
        print("▄▄▀")
        customForeground(color3[0], color3[1], color3[2])
        colorBackground("negro")
        gotoxy(x,y+3)
        print("█  █")
        gotoxy(x,y+4)
        print("▀  ▀")
    elif (letra == 'S'):
        customForeground(color1[0], color1[1], color1[2])
        print("▄▀▀▀")
        gotoxy(x,y+1)
        customBackground(color2[0], color2[1], color2[2])
        print("▀")
        colorForeground("negro")
        gotoxy(x+1, y+2)
        print("▄▄▀")
        customForeground(color3[0], color3[1], color3[2])
        colorBackground("negro")
        gotoxy(x+3,y+3)
        print("█")
        gotoxy(x,y+4)
        print("▀▀▀")
    elif (letra == 'T'):
        customForeground(color1[0], color1[1], color1[2])
        print("▀▀█▀▀")
        customBackground(color2[0], color2[1], color2[2])
        gotoxy(x+2,y+1)
        print("▀")
        gotoxy(x+2,y+2)
        print(" ")
        colorBackground("negro")
        customForeground(color3[0], color3[1], color3[2])
        gotoxy(x+2,y+3)
        print("█")
        gotoxy(x+2,y+4)
        print("▀")
    elif (letra == 'U'):
        customForeground(color1[0], color1[1], color1[2])
        print("█   █")
        gotoxy(x,y+1)
        customBackground(color2[0], color2[1], color2[2])
        print("▀")
        gotoxy(x+4,y+1)
        print("▀")
        gotoxy(x,y+2)
        print(" ")
        gotoxy(x+4,y+2)
        print(" ")
        customForeground(color3[0], color3[1], color3[2])
        colorBackground("negro")
        gotoxy(x,y+3)
        print("█")
        gotoxy(x+4,y+3)
        print("█")
        gotoxy(x+1,y+4)
        print("▀▀▀")
    elif (letra == 'V'):
        customForeground(color1[0], color1[1], color1[2])
        print("█   █")
        gotoxy(x,y+1)
        customBackground(color2[0], color2[1], color2[2])
        print("▀")
        gotoxy(x+4,y+1)
        print("▀")
        gotoxy(x,y+2)
        print(" ")
        gotoxy(x+4,y+2)
        print(" ")
        customForeground(color3[0], color3[1], color3[2])
        colorBackground("negro")
        gotoxy(x+1,y+3)
        print("█ █")
        gotoxy(x+2,y+4)
        print("▀")
    elif (letra == 'W'):
        customForeground(color1[0], color1[1], color1[2])
        print("█     █")
        gotoxy(x,y+1)
        customBackground(color2[0], color2[1], color2[2])
        print("▀")
        gotoxy(x+6,y+1)
        print("▀")
        gotoxy(x,y+2)
        print(" ")
        gotoxy(x+6,y+2)
        print(" ")
        customForeground(color3[0], color3[1], color3[2])
        colorBackground("negro")
        gotoxy(x+1,y+3)
        print("█ █ █")
        gotoxy(x+2,y+4)
        print("▀ ▀")
    elif (letra == 'X'):
        customForeground(color1[0], color1[1], color1[2])
        print("█   █")
        gotoxy(x+1,y+1)
        print("▀ ▀")
        customBackground(color2[0], color2[1], color2[2])
        colorForeground("negro")
        gotoxy(x+2, y+1)
        print("▀")
        gotoxy(x+1, y+2)
        print(" █ ")
        customForeground(color3[0], color3[1], color3[2])
        colorBackground("negro")
        gotoxy(x,y+3)
        print("█   █")
        gotoxy(x,y+4)
        print("▀   ▀")
    elif (letra == 'Y'):
        customForeground(color1[0], color1[1], color1[2])
        print("█   █")
        customBackground(color2[0], color2[1], color2[2])
        gotoxy(x+1,y+1)
        print("▀")
        gotoxy(x+3,y+1)
        print("▀")
        colorForeground("negro")
        gotoxy(x+2, y+2)
        print(" ")
        customForeground(color3[0], color3[1], color3[2])
        colorBackground("negro")
        gotoxy(x+2, y+3)
        print("█")
        gotoxy(x+2, y+4)
        print("▀")
    elif (letra == 'Z'):
        customForeground(color1[0], color1[1], color1[2])
        print("▀▀▀▀█")
        gotoxy(x+3,y+1)
        print("▀")
        customBackground(color2[0], color2[1], color2[2])
        colorForeground("negro")
        gotoxy(x+2, y+1)
        print("▀")
        colorForeground("negro")
        gotoxy(x+1, y+2)
        print("▀▄")
        customForeground(color3[0], color3[1], color3[2])
        colorBackground("negro")
        gotoxy(x,y+3)
        print("█")
        gotoxy(x,y+4)
        print("▀▀▀▀▀")
    elif (letra == '*'):
        customForeground(color1[0], color1[1], color1[2])
        print("▀▄█▄▀")
        gotoxy(x,y+1)
        print("▀")
        gotoxy(x+4,y+1)
        print("▀")
        customBackground(color2[0], color2[1], color2[2])
        gotoxy(x+1, y+1)
        print("▀▀▀")
        colorForeground("negro")
        gotoxy(x, y+2)
        print("▄█▄█▄")
        gotoxy(x,y+4)
        print("")
    elif (letra == '-'):
        customForeground(color2[0], color2[1], color2[2])
        gotoxy(x+1, y+2)
        print("▀▀▀")
        colorForeground("negro")
        gotoxy(x,y+4)
        print("")
    colorDefault()
    
        