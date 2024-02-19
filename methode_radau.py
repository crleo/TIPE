import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#paramètres constants du problème
I = 4.5e-4
J = 7e-4
Cx = -20
d = 0.001
T2 = 2

def f1(x1, x2, x3, v1, v2, v3, t):
    return v1*v2*(np.sin(x1)/np.cos(x2)) + I/J * v3 * v2 * (np.cos(x1)/np.cos(x2))

def f2(x1, x2, x3, v1, v2, v3, t):
    return  - v1*v2*(np.cos(x2)-np.sin(x1))/np.cos(x1) - J*(v1**2)*np.sin(x2) - (I/J)*v3*v1/np.cos(x1) - (d*T2/J*np.cos(x1))*np.cos(x2)

def f3(x1, x2, x3, v1, v2, v3, t):
    return  - v1*v2*(np.cos(x1)-np.cos(x1)*np.cos(x2)) - (v1**2)*np.sin(x1)*np.sin(x2) - (Cx/I) + (d*T2/I)*np.sin(x2)*np.cos(x1)


# Définir les équations différentielles
def system(t, y):
    x1, v1, x2, v2, x3, v3 = y
    dx1dt = v1
    dv1dt = f1(x1, x2, x3, v1, v2, v3, t)  
    dx2dt = v2
    dv2dt = f2(x1, x2, x3, v1, v2, v3, t) - dv1dt * np.sin(x2)*(np.sin(x1)/np.cos(x1))  
    dx3dt = v3
    dv3dt = f3(x1, x2, x3, v1, v2, v3, t) - dv2dt*np.sin(x1) + dv1dt*np.sin(x2)*np.cos(x1) 
    return [dx1dt, dv1dt, dx2dt, dv2dt, dx3dt, dv3dt]

# Conditions initiales
y0 = [0, 0, 0, 0, 0, 250]

# Intervalle de temps
t = (0, 10)

# Résoudre le système d'équations différentielles
solution = solve_ivp(system, t, y0, method='DOP853')

# Tracer la solution
plt.figure()
plt.plot(solution.t, solution.y[0], label='x1(t)')
plt.plot(solution.t, solution.y[2], label='x2(t)')
plt.plot(solution.t, solution.y[4], label='x3(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.savefig('solutionDOP853.png')