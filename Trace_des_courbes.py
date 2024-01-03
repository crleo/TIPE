##Tracé des courbes (avec paramètres)
import numpy as np
import matplotlib.pyplot as plt
plt.close()

#initialisation des valeurs

pi = np.pi
f = 0.12
Jd = 5e-4
T_2 = 5
R = 1.17e-2
w0 = 150
m = 247e-3

#définition des fonctions

def V_Ang_G(t ,T2 , fd , J ):
    return (R*(T2/J)*(np.exp(-2*pi*fd)-1))*t + w0

def V_Ang_NG(t , T2 , fd , J ):
    return (-9.81/R + (T2/(R*m))*(np.exp(2*pi*fd)-1))*t

def temps_glissement( T2 , fd , J , w ):
    return w*(1/((-9.81/R) + (T2/(R*m))*(np.exp(2*pi*fd)-1) + R*(T2/J)*(1-np.exp(-2*pi*fd))))

#initialisation des listes de valeurs

lst_t = [0.12*i for i in range(25)]
lst_T2 = [2.16 + i*0.025 for i in range(125)] #tracés à T2 variable
lst_w = [100 + i*0.25 for i in range(400)] #tracés à w variable
lst_f = [0.078 + i*0.0025 for i in range(750)] # influence de f
lst_J = [4e-4 + i*5e-7 for i in range(400)]

#création des listes des tracés

C1 = [V_Ang_G(i,T_2,f,Jd) for i in lst_t] #courbe à T2 fixé : visualisation de la zone de glissement
C1bis = [V_Ang_NG(i,T_2,f,Jd) for i in lst_t]

C2 = [temps_glissement( i , f , Jd ,w0) for i in lst_T2] #courbe à T2 variable : durée de glissement en fonction de T2

C3 = [temps_glissement( T_2 , f , Jd , i) for i in lst_w] #courbe à w variable : durée de glissement en fonction de w

C4 = [temps_glissement( T_2 , i , Jd , w0 ) for i in lst_f]

C5 = [V_Ang_G(i,T_2,0.06,Jd) for i in lst_t]
C5bis = [V_Ang_NG(i,T_2,0.06,Jd) for i in lst_t]

C6 = [temps_glissement( T_2 , f , i , w0 ) for i in lst_J]

C7 = [temps_glissement( i , 0.12 , Jd ,w0) for i in lst_T2]
C7bis = [temps_glissement( i , 0.13 , Jd ,w0) for i in lst_T2]
C7tierce = [temps_glissement( i , 0.14 , Jd ,w0) for i in lst_T2]

#tracés

plt.figure("visualisation de la zone de glissement")
plt.xlabel("Vitesses angulaire (réelle et théorique) (rad.s-1)")
plt.ylabel("temps (s)")
plt.plot(lst_t,C1,color ='red' )
plt.plot(lst_t,C1bis,color ='purple')
plt.savefig("fig_1.png")

plt.figure("durée de glissement en fonction de T2")
plt.xlabel("tension appliquée (N)")
plt.ylabel("durée de glissement (s)")
plt.plot(lst_T2,C2)
plt.savefig("fig_2.png")

plt.figure("durée de glissement en fonction de w")
plt.xlabel("vitesse angulaire (rad.s-1)")
plt.ylabel("durée de glissement (s)")
plt.plot(lst_w,C3)
plt.savefig("fig_3.png")

plt.figure("durée de glissement en fontion de f")
plt.xlabel("valeur de f")
plt.ylabel("durée de glissement (s)")
plt.plot(lst_f,C4)
plt.savefig("fig_4.png")

plt.figure("visualisation de la zone de glissement en fonction de f")
plt.xlabel("t (s)")
plt.ylabel("v/R et w (rad/s) ")
plt.plot(lst_t,C5,color = 'red')
plt.plot(lst_t,C5bis,color = 'purple')
plt.savefig("fig_5.png")

plt.figure("durée de glissement en fontion de J")
plt.xlabel("valeur de J")
plt.ylabel("durée de glissement (s)")
plt.plot(lst_J,C6)
plt.savefig("fig_6.png")

plt.figure("comparaison valeurs de f pour la durée en fonction de T2")
plt.xlabel("tension appliquée (N)")
plt.ylabel("durée de glissement (s)")
plt.plot(lst_T2,C7,color = 'red')
plt.plot(lst_T2,C7bis,color = 'blue')
plt.plot(lst_T2,C7tierce,color = 'purple')
plt.savefig("fig_7.png")

plt.show()
