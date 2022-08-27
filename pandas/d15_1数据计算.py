from warnings import simplefilter
simplefilter(action="ignore",category=FutureWarning)
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
s=pd.read_excel('数据排序.xlsx')
# print(s)
#    姓名  语文  数学  英语
# 0  张三    87    88    99
# 1  李四    84    87    91
# 2  王五    87    89    79
# 3  小虎    81    90    91
# 4  小红    80    94    78
# 5  小明    89    90    5
print('-------------------------------------------------------------求和')
s['总成绩']=s.sum(axis=1)
print(s)
print('-------------------------------------------------------------求均值')
s.loc['6']=['均值']+list(s.iloc[0:6,1:].mean(axis=0))
print(s)
print('-------------------------------------------------------------最大值')
s.loc['7']=['最大值']+list(s.iloc[0:6,1:].max(axis=0))
print(s)
print('-------------------------------------------------------------最小值')
s.loc['8']=['最低分']+list(s.iloc[0:6,1:].min())
print(s)
print('-------------------------------------------------------------中位数')
s.loc['9']=['中位数']+list(s.iloc[0:6,1:].median())
print(s)
print('-------------------------------------------------------------众数')
s.loc['10']=['众数']+list(s.iloc[0:6,1:].mode().loc[0])
print(s)
print('-------------------------------------------------------------方差')
# var()





