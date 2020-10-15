# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:30:34 2020
@author: Gyan Krishna
Demonstration of pie charts
"""
import matplotlib.pyplot as plt

labels = 'bob', 'charlie', 'alice', 'jake',
sizes = [20, 54, 16, 10]
explode = (0, 0.1, 0, 0)

plt.pie(sizes, explode, labels)
plt.show()
