import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Définir le système d'équations différentielles
def systeme(Y, t, sigma, rho):
    x, y, z = Y
    dx_dt = sigma + rho * z
    dy_dt = - rho*y*(1/x)
    dz_dt = rho*(1/x)
    return [dx_dt, dy_dt, dz_dt]

# Paramètres
sigma = -20
rho = 4.4

# Conditions initiales
Y0 = [250, 0, 0]

# Intervalle de temps
t = np.linspace(0, 13, 1000)

# Résoudre le système d'équations différentielles
solution = odeint(systeme, Y0, t, args=(sigma, rho))

# Tracer la solution
#plt.plot(t, solution[:, 0], label='x(t)')
plt.plot(t, solution[:, 1], label='y(t)')
plt.plot(t, solution[:, 2], label='z(t)')
plt.legend()
plt.show()
plt.savefig('resolution systemediff.png')