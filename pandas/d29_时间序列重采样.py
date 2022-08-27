import pandas as pd
s=pd.date_range(start='2022-1-1',periods=9,freq='T')
a=pd.Series(data=range(9),index=s)
print(a)
print('--------------------------------------产生3分钟的序列')
a=a.resample(rule='3T').sum()
print(a)










