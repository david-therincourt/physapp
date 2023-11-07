import numpy as np
import matplotlib.pyplot as plt
from physapp import markdownTable

##### IMPORTATION DONNEES CSV ######
f, Ue, Us, phi = np.loadtxt('data.csv', delimiter='\t', skiprows=2, unpack=True)
T = Us/Ue

data = [f, Ue, Us, T, phi]
header = ['f (Hz)', 'U_e (V)', 'U_s (V)', 'T', 'phi (°)']

table = markdownTable(data, header, nb_round=3)
print(table)