import numpy as np
import matplotlib.pyplot as plt
from physapp import markdown_table

##### IMPORTATION DONNEES CSV ######
f, Ue, Us, phi = np.loadtxt('data.csv', delimiter='\t', skiprows=2, unpack=True)
T = Us/Ue


#table = markdown_table(f, Ue, Us, T, phi )
table = markdown_table(f, Ue, Us, T, phi, header=["f (Hz)", "U_e (V)", "U_s (V)", "T", "phi (°)"])
print(table)