import tushare as ts
import numpy as np
import matplotlib.pyplot as plt

ts.set_token('3fce39aaf5fa27aeb3878ca532433a7d0ccde5d44210c9e9652cbb29')
pro = ts.pro_api()

# df = pro.stock_company() # 获取股票信息

df1 = pro.daily(ts_code='000001.SZ', start_date='20190001', end_date='20210625')
df2 = pro.daily(ts_code='600519.SH', start_date='20190001', end_date='20210625')

plt.subplot(2, 1, 1)
plt.grid()
plt.plot(range(df1.shape[0]), df1['open'][::-1], label='000001.SZ')
plt.legend(loc='best')

plt.subplot(2, 1, 2)
plt.grid()
plt.plot(range(df2.shape[0]), df2['open'][::-1], label='600519.SH')
plt.legend(loc='best')

plt.show()
