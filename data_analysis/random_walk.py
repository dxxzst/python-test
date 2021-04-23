from random import choice
import matplotlib.pyplot as plt


class RandomWalk:
    """随机漫步 类"""

    def __init__(self, num_points=5000):
        # 随机数目
        self.__num_points = num_points

        # x y起始点
        self.__x_values = [0]
        self.__y_values = [0]

    def fill_walk(self):
        """添加随机"""
        while len(self.__x_values) < self.__num_points:
            # 生成x\y 随机距离
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            x = self.__x_values[-1] + x_step
            y = self.__y_values[-1] + y_step
            self.__x_values.append(x)
            self.__y_values.append(y)

    def show_walk(self):
        """绘图 walk"""
        plt.style.use('ggplot')  # 设置style: plt.style.available
        fig, ax = plt.subplots(figsize=(16, 9))
        ax.scatter(self.__x_values, self.__y_values,
                   c=range(self.__num_points), cmap=plt.cm.Blues, edgecolors='none', s=10)

        # 突出显示 起始点 结束点
        ax.scatter(0, 0, c='green', edgecolors='none', s=100)
        ax.scatter(self.__x_values[-1], self.__y_values[-1], c='red', edgecolors='none', s=100)

        # 隐藏坐标轴
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
        plt.show()


if __name__ == "__main__":
    new_walk = RandomWalk(50_000)
    new_walk.fill_walk()
    new_walk.show_walk()
