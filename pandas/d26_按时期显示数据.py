import pandas as pd
s=pd.read_excel('d24_数据.xlsx')
s=s.sort_values(by=['日期'])
s=s.set_index('日期')
print(s)
print('------------------------------------------------------------------按年-')
s1=s.to_period('A')
print(s1)
print('------------------------------------------------------------------按季度-')
s1=s.to_period('Q')
print(s1)
print('------------------------------------------------------------------按月-')
s1=s.to_period('M')
print(s1)
print('------------------------------------------------------------------按星期-')
s1=s.to_period('W')
print(s1)
print('------------------------------------------------------------------按天-')
s1=s.to_period('D')
print(s1)
