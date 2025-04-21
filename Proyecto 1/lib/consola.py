import os

def enable_ansi_escape():
    if os.name == 'nt':
        import ctypes
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
        mode = ctypes.c_ulong()
        kernel32.GetConsoleMode(handle, ctypes.byref(mode))
        mode.value |= 0x0004  # ENABLE_VIRTUAL_TERMINAL_PROCESSING
        kernel32.SetConsoleMode(handle, mode)

def gotoxy(x, y):
    print(f"\033[{y};{x}H", end='')

def clrscr():
    # ANSI escape code para limpiar pantalla y mover cursor a la esquina superior izquierda
    comando = "cls" if os.name == "nt" else "clear"
    os.system(comando)