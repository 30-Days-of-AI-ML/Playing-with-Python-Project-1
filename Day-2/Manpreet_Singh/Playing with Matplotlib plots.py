
# 1 Linear Graph

import matplotlib.pyplot as plt

x1 = range(10)
plt.plot(x1, [xi * 2 for xi in x1])
plt.show()

# 2 Pie-Chart

days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]
slices = [7, 2, 2, 13, 4]
gaming = [9, 7, 6, 8, 3]
activities = ['sleeping', 'eating', 'working', 'playing', 'gaming']
cols = ['c', 'm', 'r', 'b', 'y']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90, shadow=True,
        explode=(0, 0.1, 0, 0, 0),
        autopct='%1.1f%%')

plt.title('Pie Plot')
plt.show()

# 3 Scatter Plot

x = [2, 4, 2, 2.5, 3, 3.5, 3.6]
y = [7.5, 8, 8.5, 9, 9.5, 10, 10.5]

x1 = [8, 6, 9, 9.5, 10, 10.5, 11]
y1 = [6, 5, 3.7, 4, 4.5, 5, 5.2]

plt.scatter(x, y, label='high budget low expenditure', color='r')
plt.scatter(x1, y1, label='low budget high expenditure', color='y')
plt.xlabel('Budget * 1000')
plt.ylabel('Expenditure * 1000')
plt.legend()
plt.show()
