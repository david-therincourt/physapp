import numpy as np
import matplotlib.pyplot as plt
from physapp.csv import load_oscillo_csv
from physapp import integrale

t, u = load_oscillo_csv('csv/data_integre.csv')

f = 125
T = 1/f

aire = integrale(u, t, 0, T, plot_ax=plt)
print("aire = {:.2e}".format(aire))
moy = aire/T
print("moy = {:.2f} V".format(moy))

plt.plot(t, u)
plt.axhline(moy, ls="--", color="C3")
plt.text(0.65*T, moy+0.2, "Moy = {:.2f} V".format(moy), color="C3")
plt.grid()
plt.show()