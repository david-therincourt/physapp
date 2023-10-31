import matplotlib.pyplot as plt
from physique.csv import load_avimeca3_txt

t, x, y = load_avimeca3_txt('data1_avimeca3.txt')

plt.plot(x,y,'.')
plt.title("Trajectoire d'un ballon")
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.savefig("exemple_2.png")
plt.show()
