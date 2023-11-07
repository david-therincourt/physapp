import numpy as np
import matplotlib.pyplot as plt
from physique import load_oscillo_csv, integre

t, u = load_oscillo_csv('scope_integre.csv')

f = 125
T = 1/f
aire = integre(t, u, 0, T, plot_ax=plt)
moy = aire/T


plt.plot(t, u)
plt.axhline(moy, ls="--", color="C3")
plt.text(0.65*T, moy+0.2, "Moy = {:.2f} V".format(moy), color="C3")
plt.title("Valeur moyenne d'un signal périodique")
plt.xlabel("t (s)")
plt.ylabel("u (V)")
plt.grid()
plt.savefig("exemple_3.png")
plt.show()