import tushare as ts

ts.set_token('3fce39aaf5fa27aeb3878ca532433a7d0ccde5d44210c9e9652cbb29')
pro = ts.pro_api()

df = pro.stock_company()
print(df)
