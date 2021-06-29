import matplotlib.pyplot as plt
import numpy as np

nbPoints = 500
x = np.random.standard_normal(nbPoints)
y = np.random.standard_normal(nbPoints)

# 固定种子
np.random.seed(19680801)
colors = np.random.rand(nbPoints)

area = (10 * np.random.rand(nbPoints)) ** 2

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()
