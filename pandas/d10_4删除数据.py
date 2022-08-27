import pandas as pd
data=[[45,65,200],[89,69,42],[58,74,39]]
index=['张三','李四','王五']
col=['语文','数学','英语']
s=pd.DataFrame(data=data,index=index,columns=col)
print(s)
#     语文  数学   英语
# 张三  45  65  200
# 李四  89  69   42
# 王五  58  74   39
print('------------------------------------------------------------------删除列数据')
s.drop(['语文'],axis=1,inplace=True)
print(s)
#     数学   英语
# 张三  65  200
# 李四  69   42
# 王五  74   39
s.drop(columns='英语',inplace=True)
print(s)
#      英语
# 张三  200
# 李四   42
# 王五   39
s.drop(labels='数学',axis=1,inplace=True)
print(s)
# Empty DataFrame
# Columns: []
# Index: [张三, 李四, 王五]
print('------------------------------------------------------------删除行数据')
s.drop(['张三'],axis=0,inplace=True)
print(s)
# Empty DataFrame
# Columns: []
# Index: [李四, 王五]
s.drop(index='李四',inplace=True)
print(s)
# Empty DataFrame
# Columns: []
# Index: [王五]
s.drop(labels='王五',axis=0,inplace=True)
print(s)
# Empty DataFrame
# Columns: []
# Index: []

data=[[45,65,200],[89,69,42],[58,74,39]]
index=['张三','李四','王五']
col=['语文','数学','英语']
s=pd.DataFrame(data=data,index=index,columns=col)

print('------------------------------------------------------------条件删除')
# print(s[s['语文']<=60])
#     语文  数学   英语
# 张三  45  65  200
# 王五  58  74   39
s.drop(s[s['语文']<=60].index[0],inplace=True)#语文成绩中小于60的，有张三和王五，删除行索索引1的王五
print(s)
















