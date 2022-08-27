import pandas as pd
# fp=pd.read_excel(r'C:\Users\xiaoxin15\Desktop\太谷美食商家数据.xlsx',sheet_name=0,header=None)
# print(fp)
# 导入指定列数据
# 多列
pd.set_option('display.unicode.east_asian_width',True)
# fp=pd.read_excel('美团商家数据.xlsx',sheet_name=0,usecols=['店铺名','饮食类型'])
#一列
p=pd.read_excel('美团商家数据.xlsx',sheet_name=0,usecols=[0,1])
print(p)