import matplotlib.pyplot as plt
from physapp.modelisation import ajustement_parabolique

x = [0.003,0.141,0.275,0.410,0.554,0.686,0.820,0.958,1.089,1.227,1.359,1.490,1.599,1.705,1.801]
y = [0.746,0.990,1.175,1.336,1.432,1.505,1.528,1.505,1.454,1.355,1.207,1.018,0.797,0.544,0.266]

modele = ajustement_parabolique(x, y)
print(modele)

plt.plot(x, y, '+', label="Mesures")
modele.plot()                        # Trace la courbe du modèle         
#modele.legend()                     # Affiche la légende du modèle
plt.legend()
plt.title("Trajectoire d'un ballon")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.grid()
plt.show()
