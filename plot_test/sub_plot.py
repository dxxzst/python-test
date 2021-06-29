import matplotlib.pyplot as plt
import numpy as np

fig, axes_lst = plt.subplots(2, 2)
x = np.linspace(0, 2 * np.pi, 400)
y00 = np.cos(x ** 2)
y01 = np.cos(x)
y10 = np.sin(x)
y11 = np.sin(x ** 2)

axes_lst[0, 0].plot(x, y00)
axes_lst[0, 1].plot(x, y01)
axes_lst[1, 0].plot(x, y10)
axes_lst[1, 1].plot(x, y11)

plt.show()
