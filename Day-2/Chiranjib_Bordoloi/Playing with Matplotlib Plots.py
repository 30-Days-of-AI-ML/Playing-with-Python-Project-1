#!/usr/bin/env python
# coding: utf-8


# initialization
import matplotlib.pyplot as plt

# %matplotlib inline

# Simple Graph
x = [0, 0, 5, 10, 10, 15]
y = [0, 10, 5, 10, 0, 0]
plt.plot(x, y)
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
plt.title('Simple Graph')
plt.show()

# Pie-Chart
shopping_weight = ['Fruits', 'Vegetables', 'Cloths', 'Grocery']
percentage = [9, 12, 5, 20]
plt.pie(percentage, labels=shopping_weight, radius=1.5, autopct='%1.1f%%')
plt.title('PieChart')
# plt.legend()
plt.show()

# Scatter-Plot

x1 = [1, 2, 7, 4, 5, 6, 7, 8, 8]
y1 = [3, 5, 6, 8, 6, 9, 1, 2, 10]
plt.scatter(x1, y1, color="red", marker="*")
plt.title('Random Scattered Points')
plt.show()

# Bar-Graph

plt.barh(range(len(x1)), x1)
plt.title('Bargraph')
plt.show()
