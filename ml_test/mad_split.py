import ntpath
from os import path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

HS300_STK = ['000001.SZ', '000002.SZ', '000063.SZ', '000066.SZ', '000069.SZ',
             '000100.SZ', '000157.SZ', '000166.SZ', '000333.SZ', '000338.SZ',
             '000425.SZ', '000538.SZ', '000568.SZ', '000596.SZ', '000625.SZ',
             '000651.SZ', '000656.SZ', '000661.SZ', '000703.SZ', '000708.SZ',
             '000725.SZ', '000728.SZ', '000768.SZ', '000776.SZ', '000783.SZ',
             '000786.SZ', '000800.SZ', '000858.SZ', '000860.SZ', '000876.SZ',
             '000895.SZ', '000938.SZ', '000963.SZ', '000977.SZ', '001979.SZ',
             '002001.SZ', '002007.SZ', '002008.SZ', '002024.SZ', '002027.SZ',
             '002032.SZ', '002044.SZ', '002049.SZ', '002050.SZ', '002120.SZ',
             '002129.SZ', '002142.SZ', '002153.SZ', '002157.SZ', '002179.SZ',
             '002202.SZ', '002230.SZ', '002236.SZ', '002241.SZ', '002252.SZ',
             '002271.SZ', '002304.SZ', '002311.SZ', '002352.SZ', '002371.SZ',
             '002384.SZ', '002410.SZ', '002414.SZ', '002415.SZ', '002456.SZ',
             '002460.SZ', '002463.SZ', '002475.SZ', '002493.SZ', '002508.SZ',
             '002555.SZ', '002558.SZ', '002594.SZ', '002600.SZ', '002601.SZ',
             '002602.SZ', '002607.SZ', '002624.SZ', '002673.SZ', '002714.SZ',
             '002736.SZ', '002739.SZ', '002773.SZ', '002812.SZ', '002821.SZ',
             '002841.SZ', '002916.SZ', '002938.SZ', '002939.SZ', '002945.SZ',
             '003816.SZ', '300003.SZ', '300014.SZ', '300015.SZ', '300033.SZ',
             '300059.SZ', '300122.SZ', '300124.SZ', '300136.SZ', '300142.SZ',
             '300144.SZ', '300274.SZ', '300347.SZ', '300408.SZ', '300413.SZ',
             '300433.SZ', '300450.SZ', '300498.SZ', '300529.SZ', '300558.SZ',
             '300595.SZ', '300601.SZ', '300628.SZ', '300676.SZ', '300677.SZ',
             '600000.SH', '600009.SH', '600010.SH', '600011.SH', '600015.SH',
             '600016.SH', '600018.SH', '600019.SH', '600025.SH', '600028.SH',
             '600029.SH', '600030.SH', '600031.SH', '600036.SH', '600048.SH',
             '600050.SH', '600061.SH', '600079.SH', '600085.SH', '600104.SH',
             '600109.SH', '600111.SH', '600115.SH', '600118.SH', '600132.SH',
             '600143.SH', '600150.SH', '600161.SH', '600176.SH', '600183.SH',
             '600196.SH', '600233.SH', '600276.SH', '600299.SH', '600309.SH',
             '600332.SH', '600340.SH', '600346.SH', '600352.SH', '600362.SH',
             '600383.SH', '600406.SH', '600426.SH', '600436.SH', '600438.SH',
             '600482.SH', '600489.SH', '600519.SH', '600521.SH', '600522.SH',
             '600547.SH', '600570.SH', '600584.SH', '600585.SH', '600588.SH',
             '600600.SH', '600606.SH', '600655.SH', '600660.SH', '600690.SH',
             '600703.SH', '600705.SH', '600741.SH', '600745.SH', '600760.SH',
             '600763.SH', '600795.SH', '600809.SH', '600837.SH', '600845.SH',
             '600848.SH', '600872.SH', '600886.SH', '600887.SH', '600893.SH',
             '600900.SH', '600918.SH', '600919.SH', '600926.SH', '600958.SH',
             '600989.SH', '600999.SH', '601006.SH', '601009.SH', '601012.SH',
             '601021.SH', '601066.SH', '601077.SH', '601088.SH', '601100.SH',
             '601108.SH', '601111.SH', '601138.SH', '601155.SH', '601162.SH',
             '601166.SH', '601169.SH', '601186.SH', '601211.SH', '601216.SH',
             '601225.SH', '601229.SH', '601231.SH', '601236.SH', '601238.SH',
             '601288.SH', '601318.SH', '601319.SH', '601328.SH', '601336.SH',
             '601360.SH', '601377.SH', '601390.SH', '601398.SH', '601555.SH',
             '601600.SH', '601601.SH', '601607.SH', '601618.SH', '601628.SH',
             '601633.SH', '601658.SH', '601668.SH', '601669.SH', '601688.SH',
             '601696.SH', '601698.SH', '601727.SH', '601766.SH', '601788.SH',
             '601799.SH', '601800.SH', '601808.SH', '601816.SH', '601818.SH',
             '601838.SH', '601857.SH', '601872.SH', '601877.SH', '601878.SH',
             '601881.SH', '601888.SH', '601899.SH', '601901.SH', '601916.SH',
             '601919.SH', '601933.SH', '601939.SH', '601985.SH', '601988.SH',
             '601989.SH', '601990.SH', '601995.SH', '601998.SH', '603019.SH',
             '603087.SH', '603160.SH', '603195.SH', '603233.SH', '603259.SH',
             '603288.SH', '603338.SH', '603369.SH', '603392.SH', '603501.SH',
             '603517.SH', '603658.SH', '603659.SH', '603799.SH', '603806.SH',
             '603833.SH', '603882.SH', '603899.SH', '603939.SH', '603986.SH',
             '603993.SH', '688008.SH', '688009.SH', '688012.SH', '688036.SH',
             '688111.SH', '688126.SH', '688169.SH', '688363.SH', '688396.SH']

DP_STK = [
    {'code': "601318.SH", 'name': "中国平安"}, {'code': "000651.SZ", 'name': "格力电器"}, {'code': "600036.SH", 'name': "招商银行"},
    {'code': "600031.SH", 'name': "三一重工"}, {'code': "600900.SH", 'name': "长江电力"}, {'code': "601111.SH", 'name': "中国国航"}
]
ZP_STK = [
    {'code': "002594.SZ", 'name': "比亚迪"}, {'code': "600585.SH", 'name': "海螺水泥"}, {'code': "600703.SH", 'name': "三安光电"},
    {'code': "002001.SZ", 'name': "新和成"}, {'code': "601155.SH", 'name': "新城控股"}, {'code': "600332.SH", 'name': "白云山"}
]
XP_STK = [
    {'code': "603986.SH", 'name': "兆易创新"}, {'code': "300601.SZ", 'name': "康泰生物"}, {'code': "002326.SZ", 'name': "永太科技"},
    {'code': "002508.SZ", 'name': "老板电器"}, {'code': "603712.SH", 'name': "七一二"}, {'code': "603338.SH", 'name': "浙江鼎力"}
]


def hist_plot():
    # 指数分析
    mad_df1 = pd.read_csv("D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\mad_split\\ana\\split3_000001.SH.csv")
    mad_df2 = pd.read_csv("D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\mad_split\\ana\\split3_399001.SZ.csv")
    mad_df3 = pd.read_csv("D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\mad_split\\ana\\split3_399300.SZ.csv")
    mad_df1_new = pd.read_csv("D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\mad_split\\ana\\log5_000001.SH.csv")
    mad_df2_new = pd.read_csv("D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\mad_split\\ana\\log5_399001.SZ.csv")
    mad_df3_new = pd.read_csv("D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\mad_split\\ana\\log5_399300.SZ.csv")
    mad_df1 = mad_df1[mad_df1['dt'] > '2021-01-01']
    mad_df2 = mad_df2[mad_df2['dt'] > '2021-01-01']
    mad_df3 = mad_df3[mad_df3['dt'] > '2021-01-01']
    mad_df1_new = mad_df1_new[mad_df1_new['dt'] > '2021-01-01']
    mad_df2_new = mad_df2_new[mad_df2_new['dt'] > '2021-01-01']
    mad_df3_new = mad_df3_new[mad_df3_new['dt'] > '2021-01-01']

    y1 = mad_df1['l2_madlarge_actnetinflow_turnover']
    y2 = mad_df2['l2_madlarge_actnetinflow_turnover']
    y3 = mad_df3['l2_madlarge_actnetinflow_turnover']
    y1_new = mad_df1_new['l2_madlarge_actnetinflow_turnover']
    y2_new = mad_df2_new['l2_madlarge_actnetinflow_turnover']
    y3_new = mad_df3_new['l2_madlarge_actnetinflow_turnover']

    plt.bar(range(len(y1)), y1, alpha=0.5, label='split3')
    plt.bar(np.arange(len(y1_new)), y1_new, alpha=0.5, label='log5')
    plt.legend(loc='best')
    plt.title('000001.SH 上证指数')
    plt.show()

    plt.bar(range(len(y2)), y2, alpha=0.5, label='split3')
    plt.bar(np.arange(len(y2_new)), y2_new, alpha=0.5, label='log5')
    plt.legend(loc='best')
    plt.title('399001.SZ 深证成指')
    plt.show()

    plt.bar(range(len(y3)), y3, alpha=0.5, label='split3')
    plt.bar(np.arange(len(y3_new)), y3_new, alpha=0.5, label='log5')
    plt.legend(loc='best')
    plt.title('399300.SZ 沪深300')
    plt.show()


def hist_plot2():
    # 指数分析
    mad_df1 = pd.read_csv("D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\mad_split\\ana\\origin_000001.SH.csv")
    mad_df2 = pd.read_csv("D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\mad_split\\ana\\origin_399001.SZ.csv")
    mad_df3 = pd.read_csv("D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\mad_split\\ana\\origin_399300.SZ.csv")
    mad_df1 = mad_df1[mad_df1['dt'] > '2021-01-01']
    mad_df2 = mad_df2[mad_df2['dt'] > '2021-01-01']
    mad_df3 = mad_df3[mad_df3['dt'] > '2021-01-01']
    y1 = mad_df1['l2_madlarge_actnetinflow_turnover']
    y2 = mad_df2['l2_madlarge_actnetinflow_turnover']
    y3 = mad_df3['l2_madlarge_actnetinflow_turnover']

    mad_df1_new = pd.read_csv("D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\mad_split\\ana\\split3_000001.SH.csv")
    mad_df2_new = pd.read_csv("D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\mad_split\\ana\\split3_399001.SZ.csv")
    mad_df3_new = pd.read_csv("D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\mad_split\\ana\\split3_399300.SZ.csv")
    mad_df1_new = mad_df1_new[mad_df1_new['dt'] > '2021-01-01']
    mad_df2_new = mad_df2_new[mad_df2_new['dt'] > '2021-01-01']
    mad_df3_new = mad_df3_new[mad_df3_new['dt'] > '2021-01-01']
    y1_new = mad_df1_new['l2_madlarge_actnetinflow_turnover']
    y2_new = mad_df2_new['l2_madlarge_actnetinflow_turnover']
    y3_new = mad_df3_new['l2_madlarge_actnetinflow_turnover']

    plt.bar(range(len(y1)), y1, alpha=0.5, label='origin')
    plt.bar(np.arange(len(y1_new)), y1_new, alpha=0.5, label='split3')
    plt.legend(loc='best')
    plt.title('000001.SH 上证指数')
    plt.show()

    plt.bar(range(len(y2)), y2, alpha=0.5, label='origin')
    plt.bar(np.arange(len(y2_new)), y2_new, alpha=0.5, label='split3')
    plt.legend(loc='best')
    plt.title('399001.SZ 深证成指')
    plt.show()

    plt.bar(range(len(y3)), y3, alpha=0.5, label='origin')
    plt.bar(np.arange(len(y3_new)), y3_new, alpha=0.5, label='split3')
    plt.legend(loc='best')
    plt.title('399300.SZ 沪深300')
    plt.show()


def hist_plot3():
    # 从全部的因子数据集合中进行分析
    factor_path = "D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\\mad_split\\factor\\"
    split_path = path.join(factor_path, 'split_factor.csv')
    mid_path = path.join(factor_path, 'mid_factor.csv')
    split_df = pd.read_csv(split_path)
    mid_df = pd.read_csv(mid_path)

    # 随机抽取股票
    stock_list = list(set(split_df['kdcode'].values))
    random_stock = np.random.choice(stock_list)  # # "600519.SH"

    # 筛选出数据
    split_stock_df = split_df[split_df['kdcode'] == random_stock]
    mid_stock_df = mid_df[mid_df['kdcode'] == random_stock]
    y_split = split_stock_df['l2_madlarge_actnetinflow_turnover']
    y_mid = mid_stock_df['l2_madlarge_actnetinflow_turnover']

    # sub_split = y_mid - y_split
    # plt.bar(range(len(sub_split)), sub_split, alpha=0.5, label='sub')
    # plt.title(random_stock)
    # plt.show()

    # 绘图
    plt.bar(range(len(y_split)), y_split, alpha=0.5, label='split3')
    plt.bar(np.arange(len(y_mid)), y_mid, alpha=0.5, label='mid')
    plt.legend(loc='best')
    plt.title(random_stock)
    plt.show()


def hist_plot4():
    # mad_df1 = pd.read_csv("D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\mad_split\\ana\\other_origin_000001.SH.csv")
    # mad_df2 = pd.read_csv("D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\mad_split\\ana\\other_origin_399001.SZ.csv")
    # mad_df3 = pd.read_csv("D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\mad_split\\ana\\other_origin_399300.SZ.csv")
    mad_df1_new = pd.read_csv("D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\mad_split\\ana\\act_log5_000001.SH.csv")
    mad_df2_new = pd.read_csv("D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\mad_split\\ana\\act_log5_399001.SZ.csv")
    mad_df3_new = pd.read_csv("D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\mad_split\\ana\\act_log5_399300.SZ.csv")

    # y1 = mad_df1['l2_madlarge_netinflow_turnover']
    # y2 = mad_df2['l2_madlarge_netinflow_turnover']
    # y3 = mad_df3['l2_madlarge_netinflow_turnover']
    y1_new = mad_df1_new['l2_madlarge_actnetinflow_turnover']
    y2_new = mad_df2_new['l2_madlarge_actnetinflow_turnover']
    y3_new = mad_df3_new['l2_madlarge_actnetinflow_turnover']

    # plt.bar(np.arange(len(y1)), y1, alpha=0.5, label='origin')
    plt.bar(np.arange(len(y1_new)), y1_new, alpha=0.5, label='log5')
    plt.legend(loc='best')
    plt.title('MAD主力主动净流入金额 上证指数')
    plt.show()

    # plt.bar(range(len(y2)), y2, alpha=0.5, label='origin')
    plt.bar(np.arange(len(y2_new)), y2_new, alpha=0.5, label='log5')
    plt.legend(loc='best')
    plt.title('MAD主力主动净流入金额 深证成指')
    plt.show()

    # plt.bar(range(len(y3)), y3, alpha=0.5, label='origin')
    plt.bar(np.arange(len(y3_new)), y3_new, alpha=0.5, label='log5')
    plt.legend(loc='best')
    plt.title('MAD主力主动净流入金额 沪深300')
    plt.show()


def mad_plot(stk):
    # sell_mad - buy_mad 分析
    stk_mad_df = pd.read_csv("D:\Works\KanDian\DataAnalyse\LEVEL2\mad\mad_ana_stk\{}.csv".format(stk))
    print(stk_mad_df)

    mad = stk_mad_df['mad']
    buy_mad = stk_mad_df['buy_mad']
    sell_mad = stk_mad_df['sell_mad']

    sell_buy = sell_mad - buy_mad
    plt.bar(range(len(sell_buy)), sell_buy, label='sell - buy', alpha=0.5)
    plt.legend(loc='best')
    plt.title('{} sell_mad - buy_mad'.format(stk))
    plt.show()


def mad_plot2(stk):
    stk_mad_df = pd.read_csv("D:\Works\KanDian\DataAnalyse\LEVEL2\mad\mad_ana_stk\{}.csv".format(stk))
    buy_mad = stk_mad_df['buy_mad'].mean()
    sell_mad = stk_mad_df['sell_mad'].mean()
    buy_mean = stk_mad_df['buy_mean'].mean()
    sell_mean = stk_mad_df['sell_mean'].mean()

    # plt.bar(['buy_mad', 'sell_mad', 'buy_mean', 'sell_mean'], [buy_mad, sell_mad, buy_mean, sell_mean])
    plt.bar(['buy_mad', 'sell_mad'], [buy_mad, sell_mad])
    plt.title(stk)
    plt.show()


def mad_mean_plot():
    mad_df = pd.read_csv("D:\Works\KanDian\DataAnalyse\LEVEL2\mad\stock_mad_mean.csv")
    # print(mad_df)
    # 按指数筛选
    mad_df = mad_df[mad_df['kdcode'].isin(HS300_STK)]

    # stocks = ['600744.SH', '600768.SH', '600888.SH', '601333.SH', '601717.SH']
    stocks = np.random.choice(mad_df['kdcode'].values, 6)
    mad_list = []
    buy_mad_list = []
    sell_mad_list = []

    for stock in stocks:
        mad_list.append(mad_df[mad_df['kdcode'] == stock]['mad'].values[0])
        buy_mad_list.append(mad_df[mad_df['kdcode'] == stock]['buy_mad'].values[0])
        sell_mad_list.append(mad_df[mad_df['kdcode'] == stock]['sell_mad'].values[0])

    x = np.arange(len(stocks))
    x *= 2
    width = 0.35

    b1 = plt.bar(x - width, mad_list, width=0.3)
    b2 = plt.bar(x, buy_mad_list, width=0.3)
    b3 = plt.bar(x + width, sell_mad_list, width=0.3)

    plt.xticks(x, stocks)
    plt.legend((b1, b2, b3), ('mad', 'buy_mad', 'sell_mad'))

    plt.grid(True)
    plt.show()


def quantile_test():
    base_path = 'D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\\mad_split\\quantile\\'
    df = pd.read_csv(path.join(base_path, 'q_20210104.csv'))
    buy_q = df[['kdcode', 'buy_q0.2', 'buy_q0.3', 'buy_q0.4', 'buy_q0.5', 'buy_q0.6',
                'buy_q0.7', 'buy_q0.8', 'buy_q0.9', 'buy_q0.95', 'buy_q0.99']]

    sell_q = df[['kdcode', 'sell_q0.2', 'sell_q0.3', 'sell_q0.4', 'sell_q0.5', 'sell_q0.6',
                 'sell_q0.7', 'sell_q0.8', 'sell_q0.9', 'sell_q0.95', 'sell_q0.99']]

    kdcode_list = df['kdcode'].values
    rand_kdcode = np.random.choice(kdcode_list)

    buy_values = buy_q[buy_q['kdcode'] == rand_kdcode].values
    sell_values = sell_q[sell_q['kdcode'] == rand_kdcode].values

    plt.bar(np.arange(len(buy_values[0]) - 1), buy_values[0][1:], alpha=0.5, label='buy')
    plt.bar(np.arange(len(sell_values[0]) - 1), sell_values[0][1:], alpha=0.5, label='sell')
    plt.title(rand_kdcode)
    plt.legend(loc='best')
    plt.show()


def test():
    mad_df = pd.read_csv(r"D:\Works\KanDian\DataAnalyse\LEVEL2\mad\stock_mad_mean.csv")
    # 按指数筛选
    mad_df = mad_df[mad_df['kdcode'].isin(HS300_STK)]
    mad_df['sell/buy'] = mad_df['sell_mean'] / mad_df['buy_mean']

    temp_len = len(mad_df['sell/buy'])
    plt.scatter(range(temp_len), mad_df['sell/buy'], alpha=0.8, s=10)
    plt.plot([-5, temp_len + 5], [1, 1], color='r')
    # plt.bar(range(temp_len), mad_df['sell/buy'])
    plt.xlim([-5, temp_len + 5])
    plt.title('sell_mean/buy_mean 在沪深300上的分布')
    plt.show()

    mad_df['sell/buy'].plot.hist(bins=50)
    plt.title('sell_mean/buy_mean 在沪深300上的分布')
    plt.show()


def stock_plot():
    mad_df = pd.read_csv("D:\\Works\\KanDian\\DataAnalyse\\LEVEL2\\mad\mad_split\\ana\\no_log3_factor.csv")

    for stock_info in XP_STK:
        stock_code = stock_info['code']
        stock_df = mad_df[mad_df['kdcode'] == stock_code]
        y = stock_df['l2_madlarge_netinflow_turnover']
        plt.bar(range(len(y)), y, alpha=0.5, label='log3')
        plt.legend(loc='best')
        plt.title('{}({}) MAD主力净流入金额'.format(stock_info['name'], stock_code))
        plt.show()


stock_plot()
