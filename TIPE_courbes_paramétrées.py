import numpy as np
import matplotlib.pyplot as plt
import csv
plt.close()
## Valeurs expérimentales

pi = np.pi
m = 247e-3
T2 = 1.2
T2_lst = np.linspace(1.4,2.3,3)
fd = 0.10
w0 = 275
J = 4e-4
R = 1.2e-2
g = 9.81
K_lst = np.array([T2*(np.exp(2*pi*fd)-1)/247e-3 for T2 in T2_lst])
K = T2*(np.exp(2*pi*fd)-1)/247e-3
Q = R*T2/J*(1-np.exp(-pi*fd))
tau = w0/Q
t = np.linspace(0,0.7,500)
leg = [str(T2) for T2 in T2_lst]

## Vitesse de rotation

def w(t):
    return 257 -11*t

## Trajectoire du diabolo : théorie

def y(t,K):
    return 0.5*(K-g)*t**2 + R*w0*t

Z = []
for i in range(len(K_lst)):
    Z.append(y(t, K_lst[i]))

for i in range(len(Z)):
    plt.plot(t,Z[i], label = leg[i])
    plt.show()

plt.legend()

## Durée de glissement
'''
def t_g(T2) :
    t_g = w0/(-g/R + (T2*(np.exp(2*pi*fd)-1)/m)/R + R*T2/J*(1-np.exp(-2*pi*fd)))
    return t_g

Tension2 = np.linspace(0.1,15,500)
T_G = t_g(Tension2)
plt.figure('tau(T2)')
plt.plot(Tension2,T_G)
plt.show()'''

## Récupération des données expérimentales
x1 = []
y1 = []

# Lire les données du fichier CSV
with open(r'D:\travail\traj.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(plots, None)  # saute l'en-tête si présent
    for row in plots:
        x1.append(float(row[0].replace(',', '.')))
        y1.append(float(row[1].replace(',', '.')))

Y1 = y1 - np.array([y1[0] for i in range(len(y1))])

x2 = []
y2 = []

# Lire les données du fichier CSV
with open(r'D:\travail\traj2.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(plots, None)  # saute l'en-tête si présent
    for row in plots:
        x2.append(float(row[0].replace(',', '.')))
        y2.append(float(row[1].replace(',', '.')))

Y2 = y2 - np.array([y2[0] for i in range(len(y2))])

x3 = []
y3 = []

# Lire les données du fichier CSV
with open(r'D:\travail\traj_diab_noir.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(plots, None)  # saute l'en-tête si présent
    for row in plots:
        x3.append(float(row[0].replace(',', '.')))
        y3.append(float(row[1].replace(',', '.')))

Y3 = y3 - np.array([y3[0] for i in range(len(y3))])


# Tracer le graphique de superposition
plt.plot(x1, Y1)
plt.plot(x2, Y2)

# Définir le titre et les étiquettes des axes
plt.title('Trajectoire verticale du diabolo')
plt.xlabel('t')
plt.ylabel('y(t)')

#Figure expérimentale
plt.figure('Trajectoire expérimentale')
plt.plot(x1, Y1)
plt.plot(x2, Y2)
plt.plot(x3,Y3)
plt.xlabel('t')
plt.ylabel('y(t)')

## Tracés pour la vitesse angulaire

temps =  [0,7.42,13.42]
om = [257,158,78.2]

temps2 = np.linspace(0,13.42,500)
W = w(temps2)

plt.figure("Vitesse angulaire en fonction du temps")
plt.plot(temps,om,'o')
plt.plot(temps2,W)
plt.legend(["Exp","Théo"], loc = 'center left')
plt.xlabel('t')
plt.ylabel('w(t)')
plt.plot()

# Afficher les graphique
plt.show()