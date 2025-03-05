import numpy as np
import matplotlib.pyplot as plt

# Constantes
C = 1  # Exemplo de valor para C
I0 = 1  # Exemplo de valor para I0
t = np.linspace(0, 4*np.pi, 1000)  # Intervalo de tempo

# Intensidade para Δx = λ/2
I_t = 4 * I0 * np.cos((np.pi + C * t) / 2)**2

# Plotando o gráfico
plt.figure(figsize=(8, 4))
plt.plot(t, I_t, label='Intensidade $I(t)$', color='blue')
plt.title('Intensidade em função do tempo ($\Delta x = \lambda/2$)')
plt.xlabel('Tempo ($t$)')
plt.ylabel('Intensidade ($I(t)$)')
plt.axhline(y=2*I0, color='red', linestyle='--', label='Média temporal ($2I_0$)')
plt.legend()
plt.grid()
plt.show()
