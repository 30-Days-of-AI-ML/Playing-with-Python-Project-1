# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 12:13:47 2020

@author: Gyan Krishna
"""


import matplotlib.pyplot as plt
import numpy as np

fig, plots = plt.subplots(2, 2)

x = range(0, 50, 1)
xsq = []


for i in x:
    xsq.append(i**2)

x_deg = np.arange(0, np.pi * 4, 0.1)
amplitude_sin = np.sin(x_deg)
amplitude_tan = np.tan(x_deg)

# c = 10
# cir_x = np.arange(-c,c,0.1)
# cir_y_top    = []
# cir_y_bottom = []

# for i in cir_x:
#     cir_y_top.append(c**2 - i**2);
#     cir_y_bottom.append(-(c**2 - i**2));

plots[0][0].plot(x, xsq)  # y = x^2
plots[0][0].set_title('y = x^2')

plots[0][1].plot(x_deg, amplitude_sin)  # y = cos(x)
plots[0][0].set_title('y = cos(x)')

plots[1][0].plot(x_deg, amplitude_tan)  # y = tan(x)
plots[1][0].set_title('y = tan(x)')

# plots[1][1].plot(cir_x, cir_y_top)
# plots[1][1].plot(cir_x, cir_y_bottom)
# plots[1][1].set_title('a^2 + b^2 = c^2)')

plt.plot()
