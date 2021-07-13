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

# 初始化参数
theta = np.random.rand(3)


# 创建训练数据的矩阵
def to_matrix(x):
    return np.vstack([np.ones(x.shape[0]), x, x ** 2]).T


X = to_matrix(z_series)


# 预测函数
def f(x):
    return np.dot(x, theta)


def E(x, y):
    return 0.5 * np.sum((y - f(x)) ** 2)


# 均方误差
def MSE(x, y):
    return (1 / x.shape[0]) * np.sum((y - f(x)) ** 2)


# 学习率η
ETA = 0.001  # 1e-3
# 误差的差值
diff = 1
# 更新的次数
count = 0

# 重复学习
error = E(X, y_series)
# 均方误差 记录
errors = []
errors.append(MSE(X, y_series))
while diff > 1e-2:
    # 更新参数
    theta = theta - ETA * np.dot(f(X) - y_series, X)
    # 计算与上次误差
    current_error = E(X, y_series)
    diff = error - current_error
    error = current_error
    errors.append(MSE(X, y_series))

    count = count + 1
    print("第{}次 差值 = {:.4f}".format(count, diff))

# 最终验证
plt.subplot(1, 2, 1)
plt.scatter(z_series, y_series)
x = np.linspace(-3, 3, 100)
plt.plot(x, f(to_matrix(x)))

# 均方误差 逐步减小
plt.subplot(1, 2, 2)
x_errors = np.arange(len(errors))
plt.plot(x_errors, errors)
plt.show()
