import matplotlib.pyplot as plt
import numpy as np

mu = 100
sigma = 15
x = mu + sigma * np.random.randn(200)
num_bins = 25
plt.figure(figsize=(9, 6), dpi=100)

n, bins, patches = plt.hist(x, num_bins,
                            color='w', edgecolor='k',
                            hatch=r'ooo',
                            density=1,
                            label='频率')

y = (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2)

plt.plot(bins, y, '--', label='概率密度函数')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号
plt.xlabel('聪明度')
plt.ylabel('概率密度')
plt.title('IQ直方图: $\mu=100$,$\sigma=15$')

plt.legend()
plt.show()
