import pandas as pd
s=pd.date_range(start='2022-1-1',periods=12,freq='T')
a=pd.Series(data=range(12),index=s)
print(a.resample('5min').ohlc())
print('---------------------------------------移动窗口数据计算')
s=pd.date_range(start='2022-1-1',periods=12,freq='D')
a=pd.Series(data=[2,6,4,5,6,9,7,3,2,4,5,6],index=s)
print(a)
print('---------------------------------------计算3天的均值')
print(a.rolling(3,min_periods=1).mean())
# min_periods=1至少一个观测值


