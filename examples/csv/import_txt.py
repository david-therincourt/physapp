# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 23:27:11 2020
@author: david
"""

#import numpy as np
import matplotlib.pyplot as plt
from physapp.csv import load_txt

x, y = load_txt('csv/data.txt')

plt.plot(x,y,'.')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.show()
