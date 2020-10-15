# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 00:57:02 2020
@author: Gyan Krishna

plotting the following curves:-
1. y = x
2. y = x^2
3. y = x^3
4. y = log(x)
"""


import numpy as np
import matplotlib.pyplot as plt
fig, plots = plt.subplots(2, 2)

x = range(1, 100, 1)
y = []
z = []
p = []

for i in x:
    y.append(i**2)
    z.append(i**3)
    p.append(np.log(i))

plots[0][0].plot(x, y)   # y = x^2
plots[0][0].set_title('y = x^2')

plots[0][1].plot(x, z)   # y = x^3
plots[0][1].set_title('y = x^3')

plots[1][0].plot(x, p)   # y = log(x)
plots[1][0].set_title('y = log(x)')

plots[1][1].plot(x, x)   # y = x
plots[1][1].set_title('y = x')


plt.show
