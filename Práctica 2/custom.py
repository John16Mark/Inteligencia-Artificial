import gymnasium as gym
from gymnasium import Env, spaces
import pygame
import numpy as np

class CustomEnv(Env):
    def __init__(self):
        super().__init__()
        self.grid_size = (5, 4)  # 5 filas x 4 columnas
        self.cell_size = 100  # Tamaño de cada celda
        self.width = self.grid_size[1] * self.cell_size
        self.height = self.grid_size[0] * self.cell_size
        
        self.observation_space = spaces.Discrete(self.grid_size[0] * self.grid_size[1])
        self.action_space = spaces.Discrete(4)  # 0: Izq, 1: Der, 2: Arriba, 3: Abajo

        self.state = 0
        self.total = 0
        self.window = None
        self.running = True  # Control para mantener el juego abierto
        self.done = False  # Control del estado del juego

        # Inicializar pygame
        pygame.init()
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Entorno personalizado")

        # Cargar imágenes
        self.bg_texture = pygame.image.load("background.png")
        self.bg_texture = pygame.transform.scale(self.bg_texture, (self.cell_size, self.cell_size))

        self.player_texture = pygame.image.load("player.png")
        self.player_texture = pygame.transform.scale(self.player_texture, (self.cell_size, self.cell_size))

        self.goal_texture = pygame.image.load("gold.png")
        self.goal_texture = pygame.transform.scale(self.goal_texture, (self.cell_size, self.cell_size))

    def reset(self):
        self.state = 0
        self.total = 0
        self.done = False
        return self.state, {}

    def step(self, action):
        if self.done:
            return self.state, 0, self.done, False, {}

        row, col = divmod(self.state, self.grid_size[1])  # Convertir índice a coordenadas

        if action == 0 and col > 0:  # Izquierda
            col -= 1
        elif action == 1 and col < self.grid_size[1] - 1:  # Derecha
            col += 1
        elif action == 2 and row > 0:  # Arriba
            row -= 1
        elif action == 3 and row < self.grid_size[0] - 1:  # Abajo
            row += 1

        self.state = row * self.grid_size[1] + col
        reward = 10 if self.state == self.observation_space.n - 1 else 1
        self.total += reward
        self.done = self.state == self.observation_space.n - 1  # Termina si llega a la meta

        return self.state, reward, self.done, False, {}

    def render(self):
        if self.window is None:
            return  # No intentar renderizar si pygame no está inicializado

        self.window.fill((255, 255, 255))  # Fondo blanco

        for row in range(self.grid_size[0]):
            for col in range(self.grid_size[1]):
                x = col * self.cell_size
                y = row * self.cell_size
                cell_index = row * self.grid_size[1] + col

                # Dibujar la textura de fondo en todas las casillas
                self.window.blit(self.bg_texture, (x, y))

                # Dibujar la textura del jugador en la casilla actual
                if cell_index == self.state:
                    self.window.blit(self.player_texture, (x, y))

                # Dibujar la textura de la meta
                elif cell_index == self.observation_space.n - 1:
                    self.window.blit(self.goal_texture, (x, y))

        pygame.display.flip()

    def close(self):
        if self.window:
            pygame.quit()
            self.window = None


# Inicialización del entorno
env = CustomEnv()
obs, info = env.reset()

# Bucle principal de pygame
while env.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            env.running = False  # Cerrar ventana
        elif event.type == pygame.KEYDOWN and env.done:  
            if event.key == pygame.K_r:  # Presionar "R" para reiniciar
                obs, info = env.reset()  # Reiniciar el juego
                print("Juego reiniciado")

    if not env.done:  # Si el juego sigue activo, el agente sigue jugando
        action = env.action_space.sample()  # Acción aleatoria
        print(f"Acción tomada: {action}")  # Mostrar acción en consola

        obs, reward, env.done, truncated, info = env.step(action)
        env.render()
        
        pygame.time.delay(500)  # Pausar 500ms para hacer más visible el movimiento

env.close()
