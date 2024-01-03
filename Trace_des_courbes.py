import numpy as np
import matplotlib.pyplot as plt
plt.close()

def vitesse_angulaire_r(t,T_2):
    return -12.39*T_2*t + 150

def vitesse_angulaire_NG(t,T_2):
    return (387*T_2 - 838)*t

##tracé d'une seule courbe a T_2 fixé

t = [0.12*i for i in range(25)]
w = [vitesse_angulaire_r(i,2.3) for i in t]
w_ng = [vitesse_angulaire_NG(i,2.3) for i in t]

plt.figure("0")
plt.plot(t,w)
plt.plot(t,w_ng)

##intersections de vitesses
def intersection(T_2):
    T = 150*(1/(T_2*399 - 838))
    return vitesse_angulaire_r(T,T_2)

def intersectionbis(T_2):
    T = 150*(1/(T_2*399 - 838))
    return vitesse_angulaire_NG(T,T_2)

def intersection_tau(T_2):
    T = 150*(1/(T_2*399 - 838))
    return T

lst_T_2 = [2.16 + i*0.025 for i in range(75)]

intersect_lst = [intersection(i) for i in lst_T_2]
intersect_lstbis = [intersectionbis(i) for i in lst_T_2]

lst_Tmin = [2.16 + i*0.005 for i in range(500)]
intersection_lst = [intersection(i) for i in lst_Tmin]

plt.figure("01")
plt.plot(lst_T_2,intersect_lst,color="green")
plt.savefig("trace_des_courbes1.png")

plt.figure("02")
plt.plot(lst_T_2,intersect_lstbis,color="red")
plt.savefig("trace_des_courbes2.png")

plt.figure("03")
plt.plot(lst_Tmin,intersection_lst,color="purple")
plt.savefig("trace_des_courbes3.png")

plt.figure("4")
plt.plot(lst_T_2,intersect_lstbis,color="red")
plt.plot(lst_T_2,intersect_lst,color="green")
plt.savefig("trace_des_courbes4.png")

plt.figure("5")
lst_Tmin2 = [2.16 + i*0.05 for i in range(100)]
intersect_tau = [intersection_tau(i) for i in lst_Tmin2]
plt.plot(lst_Tmin2,intersect_tau,color="blue")
plt.savefig("trace_des_courbes5.png")
