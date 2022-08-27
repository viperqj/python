import pandas as pd
fp=pd.read_csv('美团商家数据.csv',encoding='utf-8')
# print(fp)
# fp=fp.set_index(['店铺名'])
# print(fp)
print('---------------------------------------------数据清洗后设置连续索引')
print(fp.drop_duplicates(['评分']))
print(fp.drop_duplicates(['评分']).reset_index(drop=True))