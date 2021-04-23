from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline


class ShaiZi:
    """定义一个骰子"""

    def __init__(self, num_sides=6):
        self.__num_sides = num_sides

    def roll(self):
        """摇骰子 返回随机数"""
        return randint(1, self.__num_sides)

    def show_result(self):
        results = []
        for num in range(1000):
            result = self.roll()
            results.append(result)

        # 分析结果 每面出现次数
        frequencies = []
        for value in range(1, self.__num_sides + 1):
            frequency = results.count(value)
            frequencies.append(frequency)

        x_values = list(range(1, self.__num_sides + 1))
        data = [Bar(x=x_values, y=frequencies)]
        x_axis_config = {'title': "结果"}
        y_axis_config = {'title': "结果的频率"}
        my_layout = Layout(title="投掷D6 1000次", xaxis=x_axis_config, yaxis=y_axis_config)
        offline.plot({"data": data, "layout": my_layout}, filename='d6.html')

    def double_result(self):
        results = []
        for num in range(1000):
            result = self.roll() + self.roll()
            results.append(result)

        # 分析结果 每面出现次数
        frequencies = []
        for value in range(1 * 2, self.__num_sides * 2 + 1):
            frequency = results.count(value)
            frequencies.append(frequency)

        x_values = list(range(1 * 2, self.__num_sides * 2 + 1))
        data = [Bar(x=x_values, y=frequencies)]
        x_axis_config = {'title': "结果", "dtick": 1}
        y_axis_config = {'title': "结果的频率"}
        my_layout = Layout(title="投掷两个D6 1000次", xaxis=x_axis_config, yaxis=y_axis_config)
        offline.plot({"data": data, "layout": my_layout}, filename='d6_d6.html')


if __name__ == "__main__":
    shai_zi = ShaiZi()
    shai_zi.double_result()
