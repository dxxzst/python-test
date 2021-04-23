from matplotlib import pyplot as plt

# 支持中文
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x_values = [x for x in range(-100, 100)]
y_values = [x ** 2 for x in x_values]

# 设置style: plt.style.available
plt.style.use('ggplot')

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# 设置图表标题
ax.set_title("平方数", fontsize=18)
ax.set_xlabel("值", fontsize=12)
ax.set_ylabel("值的平方", fontsize=12)

# 设置刻度标记的的大小
ax.tick_params(axis='both', labelsize=12)

# 保存图像
plt.savefig("scatter.png", bbox_inches='tight')

# 绘制图像
plt.show()
