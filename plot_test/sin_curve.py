import math
import numpy as np
import matplotlib.pyplot as plt

nbSamples = 256

# xRange = [-math.pi, math.pi]
# x, y = [], []
# for n in range(nbSamples):
#     ratio = (n + 0.5) / nbSamples
#     x.append(xRange[0] + (xRange[1] - xRange[0]) * ratio)
#     y.append(math.sin(x[-1]))

x = np.linspace(-math.pi, math.pi, num=nbSamples, endpoint=True)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, color='g', linewidth=4, linestyle='--', label=r'$y=sin(x)$')
plt.plot(x, y2, '*', markersize=8, markerfacecolor='r', markeredgecolor='k', label=r'$y=cos(x)$')

plt.legend(loc='best')
plt.show()
