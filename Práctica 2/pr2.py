import gymnasium as gym
import pygame

# Inicializar entorno
env = gym.make("FrozenLake-v1", render_mode="human", is_slippery=False)
obs, info = env.reset()
env.render()

# Inicializar pygame para detectar teclas
pygame.init()

# Mapeo de teclas a acciones del entorno
key_to_action = {
    pygame.K_w: 3,  # Arriba
    pygame.K_s: 1,  # Abajo
    pygame.K_a: 0,  # Izquierda
    pygame.K_d: 2   # Derecha
}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Salir si se cierra la ventana
            running = False
            done = True
        elif event.type == pygame.KEYDOWN:  # Si se presiona una tecla
            if event.key in key_to_action:
                action = key_to_action[event.key]  # Convertir tecla en acción
                obs, reward, done, truncated, info = env.step(action)
                env.render()

                print(f"Acción tomada: {action} | Nueva posición: {obs} | Recompensa: {reward}")

                if done:
                    print("Juego terminado. Presiona R para reiniciar o cierra la ventana.")
    
            elif event.key == pygame.K_r and done:  # Reiniciar con "R" si el juego terminó
                obs, info = env.reset()
                done = False
                print("Juego reiniciado")

# Cerrar entorno y pygame
env.close()
pygame.quit()