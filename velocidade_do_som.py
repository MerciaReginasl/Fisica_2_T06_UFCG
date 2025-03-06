import numpy as np
import matplotlib.pyplot as plt

# Constantes
B = 2.2e9  # Módulo de compressibilidade da água (em Pa)
rho = np.linspace(800, 1200, 100)  # Densidade (em kg/m³)

# Velocidade do som
v = np.sqrt(B / rho)

# Plotando o gráfico
plt.plot(rho, v, label=r'$v = \sqrt{\frac{B}{\rho}}$')
plt.xlabel('Densidade ($\\rho$) [kg/m³]')
plt.ylabel('Velocidade do Som ($v$) [m/s]')
plt.title('Velocidade do Som em Função da Densidade')
plt.grid(True)
plt.legend()
plt.show()
