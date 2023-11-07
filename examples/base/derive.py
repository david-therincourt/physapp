import numpy as np
import matplotlib.pyplot as plt
from physapp import derive

#### PARAMETRES ###
f = 10
w = 2*np.pi*f
T = 1/f
A = 5

#### CALCULS ####
t = np.linspace(-T, T, 200)
u = A*np.sin(w*t)
du = derive(u,t)

T = np.nanmax(du)/max(u)
print("T = ", T)
print("w = ", w, "rad/s")


#### COURBES ####
plt.subplot(211)
plt.plot(t*1000, u, label="Tension u")
plt.legend()
plt.axvline(0, color="gray")
plt.grid()

plt.subplot(212)
plt.plot(t*1000, du, label="Dérivée du/dt")
plt.legend()
plt.axvline(0, color="gray")
plt.grid()


plt.show()
