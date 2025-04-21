import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt

# Número de episodios a ejecutar
num_episodes = 100

# Almacenar las recompensas totales por episodio
rewards_per_episode = []

# Crear el entorno
env = gym.make("FrozenLake-v1", is_slippery=False)


# Graficar resultados
plt.figure(figsize=(10, 5))
plt.scatter(range(num_episodes), rewards_per_episode, marker='o', alpha=0.6, label="Éxito (1) o Fracaso (0)")
plt.yticks([0, 1])  # Solo mostrar 0 y 1 en el eje vertical
plt.xlabel("Episodio")
plt.ylabel("Éxito (1) / Fracaso (0)")
plt.title(f"Resultados de {num_episodes} episodios")
plt.legend()
plt.show()
