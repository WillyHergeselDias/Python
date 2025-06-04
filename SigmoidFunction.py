import matplotlib.pyplot as plt
import numpy as np

S = lambda x: 1/(1 + e**-x)

x = np.linspace(-6,6)
y = S(x)

plt.plot(x,y, label = "Função de Sigmoid")

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.legend()
plt.title("Sigmoid Function")
plt.show()
