import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

mad_df = pd.read_csv("D:\Works\KanDian\DataAnalyse\LEVEL2\mad\ic_diff\ic_diff.csv", index_col=[0])

# mad_df = mad_df[np.abs(mad_df['ic_mean_d1']) > 0.01]


def normal_plot_1():
    x = np.arange(mad_df.shape[0])
    y_d1 = mad_df['ic_mean_d1'].values
    y_m10 = mad_df['ic_mean_m10'].values
    y_lm = mad_df['ic_mean_lm'].values
    y_abs1 = (np.abs(mad_df['ic_mean_d1']) - np.abs(mad_df['ic_mean_m10'])).values
    y_abs2 = (np.abs(mad_df['ic_mean_d1']) - np.abs(mad_df['ic_mean_lm'])).values

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文
    plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

    plt.subplot(2, 1, 1)
    plt.grid()
    plt.ylim(-0.05, 0.05)
    plt.title('ic_mean 对比')
    plt.plot(x, y_d1, label='d1')
    plt.plot(x, y_m10, label='m10')
    plt.plot(x, y_lm, label='lm')
    plt.legend(loc='best')

    plt.subplot(2, 1, 2)
    plt.grid()
    plt.ylim(-0.05, 0.05)
    plt.title('差值')
    plt.plot(x, y_abs1, label=r'abs(d1) - abs(m10)')
    plt.plot(x, y_abs2, label=r'abs(d1) - abs(lm)')
    plt.legend(loc='best')

    plt.tight_layout()
    plt.show()


def normal_plot():
    y_d1 = mad_df['ic_mean_d1'].values
    y_m10 = mad_df['ic_mean_m10'].values
    y_lm = mad_df['ic_mean_lm'].values

    plt.plot(y_d1, y_d1, color='red')
    plt.scatter(y_d1, y_m10, label='m10')
    plt.scatter(y_d1, y_lm, label='lm')
    plt.legend(loc='best')
    plt.show()


def pd_plot():
    mad_df.plot(subplots=True, figsize=(15, 15), layout=(3, 3))
    plt.show()


def sns_plot():
    sns.set(style='ticks')
    sns.pairplot(mad_df[['ic_mean_d1', 'ic_mean_lm']], diag_kind='kde')
    plt.show()


def binomial_plot():
    # N次伯努利试验的结果分布即为二项分布。使用binomial(1,p)即为一次二项分布。
    # 使用binomial(1,p,n)即表示生成n维的二项分布数组，也就是伯努利分布
    binomial = np.random.binomial(100, 0.5, 10000)
    sns.distplot(binomial)
    plt.show()


def hist_plot():
    x = np.random.randn(1000)
    y = np.random.randn(1000)
    plt.hist2d(x, y, bins=[10, 10])
    plt.show()


def hist_plot2():
    data_n1 = np.random.normal(-1, 2, 1000)
    data_n2 = np.random.normal(0, 1, 5000)
    pd_n1 = pd.DataFrame(data_n1, columns=['normal'])
    pd_n2 = pd.DataFrame(data_n2, columns=['normal'])
    pd_n1['normal'].plot.hist(bins=30, figsize=(10, 6), alpha=0.5, density=True)
    pd_n2['normal'].plot.hist(bins=30, figsize=(10, 6), alpha=0.5, density=True)
    plt.show()


def sns_lmplot():
    sns.set(style='ticks')
    df = sns.load_dataset('anscombe')
    sns.lmplot(x='x', y='y', col='dataset', hue='dataset', data=df,
               col_wrap=2, ci=None, palette='muted', height=4,
               scatter_kws={'s': 50, 'alpha': 1})
    plt.show()


normal_plot()
