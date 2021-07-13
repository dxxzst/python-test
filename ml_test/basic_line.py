import numpy as np
import matplotlib.pyplot as plt

# 模拟一些数据
x_series = np.linspace(1, 50, 30)
y_series = []
for x in x_series:
    y_series.append(5 * x + 6 + np.random.uniform(-10, 10))

# plt.scatter(x_series, y_series)
# plt.show()

# 数据标准化 z-score规范化
z_series = (x_series - np.mean(x_series)) / np.std(x_series)
# plt.scatter(z_series, y_series)
# plt.show()

# 开始模拟 初始化参数
theta0 = np.random.rand()
theta1 = np.random.rand()


# 预测函数
def f(x):
    return theta0 + theta1 * x


def E(x, y):
    return 0.5 * np.sum((y - f(x)) ** 2)


# 学习率η
ETA = 0.001  # 1e-3
# 误差的差值
diff = 1
# 更新的次数
count = 0

error = E(z_series, y_series)
while diff > 0.001:
    temp0 = theta0 - ETA * np.sum(f(z_series) - y_series)
    temp1 = theta1 - ETA * np.sum((f(z_series) - y_series) * z_series)

    # 更新参数
    theta0 = temp0
    theta1 = temp1

    # 计算与上次误差
    current_error = E(z_series, y_series)
    diff = error - current_error
    error = current_error

    count = count + 1
    print("第{}次 theta0 = {:.3f} theta1 = {:.3f}, 差值 = {:.4f}".format(count, theta0, theta1, diff))

# 最终验证
plt.scatter(z_series, y_series)
x = np.linspace(-3, 3, 100)
plt.plot(x, f(x))
plt.show()
