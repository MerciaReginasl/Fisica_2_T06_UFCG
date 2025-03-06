import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da onda
p0 = 1.0  # Amplitude da pressão (em Pa)
k = 2 * np.pi / 1.0  # Número de onda (em m⁻¹)
omega = 2 * np.pi * 440  # Frequência angular (em rad/s), f = 440 Hz
x = 0  # Posição fixa (em metros)
t = np.linspace(0, 0.01, 500)  # Tempo (em segundos)

# Pressão em função do tempo
p = p0 * np.sin(k * x - omega * t - np.pi / 2)

# Plotando o gráfico
plt.plot(t, p, label=r'$p(x, t) = p_0 \sin(kx - \omega t - \frac{\pi}{2})$')
plt.xlabel('Tempo ($t$) [s]')
plt.ylabel('Pressão ($p$) [Pa]')
plt.title('Pressão em Função do Tempo')
plt.grid(True)
plt.legend()
plt.show()
