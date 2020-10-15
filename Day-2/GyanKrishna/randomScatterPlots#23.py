# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:37:35 2020
@author: Gyan Krishna

"""


import matplotlib.pyplot as plt
import numpy as np

np.random.seed(59498498)

N = 100
x = np.random.rand(N)
y = np.random.rand(N)

colors = np.random.rand(N)

area = (30 * np.random.rand(N))**2
plt.scatter(x, y, area, colors, alpha=0.5)
plt.show()
