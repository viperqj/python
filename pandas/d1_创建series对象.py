import pandas as pd
data=['语文','数学','英语']
s=pd.Series(data=data)
print(s)
# 0    语文
# 1    数学
# 2    英语
# dtype: object
s=pd.Series(data=data,index=['张三','李四','王五'])
print(s)
# 张三    语文
# 李四    数学
# 王五    英语
# dtype: object