import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "./data/death_valley_2018_full.csv"  # "./data/sitka_weather_07-2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)

    # 获取日期 最高温度
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[6])
            low = int(row[7])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 支持中文
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 设置style: plt.style.available
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(16, 9))

ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title("2018年每日温度", fontsize=18)
ax.set_xlabel("", fontsize=12)
ax.set_ylabel("温度（F）", fontsize=12)

# 倾斜日期标签
# fig.autofmt_xdate()

# 设置刻度标记的的大小
ax.tick_params(axis='both', which='major', labelsize=12)
plt.show()
