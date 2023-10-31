import matplotlib.pyplot as plt
from physapp.csv import load_oscillo_csv
from physapp import spectre_RMS_dBV
from mplcursors import cursor

fig, (axes1, axes2) = plt.subplots(2, 1)

t, u = load_oscillo_csv('csv/data_carre.csv')
u = u - 1.5

T = 4e-3
f, A = spectre_RMS_dBV(u, t, T)

plt.subplot(211)
plt.plot(t, u)
plt.grid()

plt.subplot(212)
plt.stem(f, A)
cursor()
plt.xlim(0, 2000)
plt.grid()
plt.show()