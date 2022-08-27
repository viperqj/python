import pandas as pd
pd.set_option('display.unicode.east_asian.width',True)
df=pd.read_excel('美团商家数据.xlsx')
# for i in range(0,10):
#     for j in range(0,8):
#         if str(df.iloc[i, j]) =='nan':
#             print(i, j)
print(df.info())#查看是否有缺失值
print('------------------判断缺失值')
print(df.isnull())
print(df.notnull())
print('-------------------------------------------------------------------------缺失值的处理方式')
print('-------------删除')
# df=df.dropna()
# print(df)
print('------------填充')
df['商圈']=df['商圈'].fillna(0)
print(df.iloc[8,4])
print('-------------------------------------------------------------------------重复值值的处理方式')
print('----判断是否有重复值')
print(df.duplicated())
print('-------------------------------删除全部重复的数据')
print(df.drop_duplicates())
print('-------------------------删除有指定列重复的全部数据')
print(df.drop_duplicates(['最低消费']))

