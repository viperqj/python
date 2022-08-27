import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
s=pd.read_excel('数据排序.xlsx')
print(s)
print('----------------------------------------------排序')
print(s.sort_values(by='语文',ascending=True))
print('----------------------------------------------排序')
print(s.sort_values(by=['语文','数学'],ascending=True))