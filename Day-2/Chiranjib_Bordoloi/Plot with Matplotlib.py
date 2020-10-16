import matplotlib.pyplot as plt
import numpy as np

# Y = X^2
x = range(-50, 50)
y = [i * i for i in x]
plt.plot(x, y)
plt.show()

# Y = COS(X)
x = np.arange(0, 4 * np.pi, 0.1)
y = np.cos(x)
plt.plot(x, y)
plt.show()

# Y = TAN(X)
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.tan(x)
plt.plot(x, y)
plt.show()
