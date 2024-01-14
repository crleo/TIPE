import numpy as np
import matplotlib.pyplot as plt

# Données
x = np.array([-0.3425,-0.1985,-0.0202,0.0198,0.1740,0.2624,0.3075,0.4511,0.5306,0.5596,0.6419,0.7324,0.8879,0.9243,1.033])
y = np.array([-0.1918,0.1631,0.3173,0.3853,0.5114,0.6227,0.6740,0.7693,0.8563,0.8971,0.9741,1.079,1.234,1.289,1.367])

# Incertitudes
x_err = np.array([0.042,0.036,0.031,0.029,0.025,0.023,0.022,0.019,0.018,0.017,0.016,0.014,0.012,0.012,0.011])  
y_err = np.array([0.03,0.025,0.021,0.020,0.018,0.016,0.015,0.014,0.013,0.012,0.011,0.010,0.009,0.008,0.008])  

# Moyennes de x et y
mean_x = np.mean(x)
mean_y = np.mean(y)

# Calculer les différences entre x, y et leurs moyennes
diff_x = x - mean_x
diff_y = y - mean_y

# Calculer la pente (m) et l'ordonnée à l'origine (c)
m = np.sum(diff_x * diff_y) / np.sum(diff_x**2)
c = mean_y - m * mean_x

# Courbe de régression
y_reg = m * x + c
equation = "y = {:.2f}x + {:.2f}".format(m, c)
print(equation)

# Tracer les données expérimentales avec incertitudes
plt.errorbar(x, y, xerr=x_err, yerr=y_err, fmt='o', color='purple', label='Données expérimentales')

# Tracer la courbe de régression
plt.plot(x, y_reg, color='red', label='Régression linéaire')

plt.xlabel('ln(T1)')
plt.ylabel('ln(T2))')
plt.show()
plt.savefig("reg_lin.png")

print("Pente (m) :", m)
print("Ordonnée à l'origine (c) :", c)