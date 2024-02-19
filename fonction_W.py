import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lambertw

# Créer un tableau de valeurs x
x = np.linspace(-100, 100, 40000)

# Calculer la fonction W de Lambert pour ces valeurs
y = lambertw(x)

# Tracer la fonction
plt.plot(x, y.real)
plt.title("Fonction W de Lambert")
plt.xlabel("x")
plt.ylabel("W(x)")
plt.grid(True)
plt.show()
plt.savefig("lambert.png")