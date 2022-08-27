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
print('----------------------------------------------直接使用列名')
print(s[['数学','英语']])
#     数学   英语
# 张三  65  200
# 李四  69   42
# 王五  74   39
print('---------------------------------------------使用loc')
print(s.loc[:,['数学','英语']])#,左边表示行,右边表示列
#     数学   英语
# 张三  65  200
# 李四  69   42
# 王五  74   39
print('----------------提取连续数据')
print(s.loc[:,'语文':])
#     语文  数学   英语
# 张三  45  65  200
# 李四  89  69   42
# 王五  58  74   39
print('---------------------------------------------使用iloc')
print(s.iloc[:,[1,2]])#,左边表示行,右边表示列
#     数学   英语
# 张三  65  200
# 李四  69   42
# 王五  74   39
print('----------------提取连续数据')
print(s.iloc[:,0:])
#     语文  数学   英语
# 张三  45  65  200
# 李四  89  69   42
# 王五  58  74   39





