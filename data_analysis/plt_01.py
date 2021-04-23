import matplotlib.pyplot as plt

# 支持中文
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 设置style: plt.style.available
plt.style.use('ggplot')

input_values = [x for x in range(-100, 100)]
squares2 = [y ** 2 for y in input_values]
squares3 = [y ** 3 for y in input_values]

fig, ax = plt.subplots()
ax.plot(input_values, squares2, linewidth=3)
# ax.plot(input_values, squares3, linewidth=3)

# 设置图表标题
ax.set_title("平方数", fontsize=18)
ax.set_xlabel("值", fontsize=12)
ax.set_ylabel("值的平方", fontsize=12)

# 设置刻度标记的的大小
ax.tick_params(axis='both', labelsize=12)
plt.show()
