import numpy as np
import matplotlib.pyplot as plt
from physapp.modelisation import ajustement_affine, ajustement_lineaire, ajustement_parabolique


# Linéaire
#x = [1.0, 2.0, 3.0, 4.0, 5.0,  6.0,  7.0,  8.0,  9.0]
#y = [2.1, 3.9, 6.2, 7.8, 9.9, 12.1, 14.0, 16.1, 17.8]

# Affine
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [2.2, 4.1, 5.9, 8.2, 9.8, 11.9, 13.1, 16, 18.1, 19.8]

# Parabole
#x = [0.003,0.141,0.275,0.410,0.554,0.686,0.820,0.958,1.089,1.227,1.359,1.490,1.599,1.705,1.801]
#y = [0.746,0.990,1.175,1.336,1.432,1.505,1.528,1.505,1.454,1.355,1.207,1.018,0.797,0.544,0.266]

#save_txt((x,y), "affine.txt")

modele = ajustement_affine(x, y)
print(modele)

modele2 = ajustement_lineaire(x,y)

plt.plot(x, y, '+r', label="Mesures")
modele.plot(ls='--')
modele.legend(loc=0)
modele2.plot()
modele2.legend()
leg = plt.legend()
plt.grid()
plt.show()
