import numpy as np
import matplotlib.pyplot as plt
from physapp.csv import load_ltspice_csv 


t, u, uC, uR = load_ltspice_csv("csv/data_ltspice.txt")

plt.plot(t, u, label=r"$u(t)$")
plt.plot(t, uC, label=r"$u_C(t)$")
plt.plot(t, uR, label=r"$u_R(t)$")
plt.legend()
plt.grid()

plt.show()