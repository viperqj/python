import pandas as pd
fp=pd.read_csv(r'C:\Users\xiaoxin15\Desktop\美食商家数据.csv',sep=',',encoding='gbk')
# gbk对应ANSI
# print(fp)
print(fp.head(5))

