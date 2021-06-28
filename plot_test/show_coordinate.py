import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 1)
y = x * 2

for a, b in zip(x, y):
    plt.text(a - 0.5, b, (a, b), ha='center', va='bottom', fontsize=10)

plt.plot(x, y, 'bo-')
plt.show()
