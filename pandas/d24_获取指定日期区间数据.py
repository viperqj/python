import pandas as pd
s=pd.read_excel('d24_数据.xlsx')
s=s.sort_values(by=['日期'])
s=s.set_index('日期')
print(s)
print(s.loc['1999'])
print(s.loc['1999-10'])
print(s.loc['1999-10-01':'2001-10-09'])











