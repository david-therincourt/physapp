#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:46:31 2019
@author: david
"""

import numpy as np
from physapp.csv import save_txt

x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([4.98, 3.59, 2.57, 1.83, 1.32, 0.93, 0.67, 0.48, 0.34, 0.25])

save_txt((x,y), fileName = "csv/export.txt")
