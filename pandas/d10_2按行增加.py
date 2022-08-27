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
print('--------------------------------------采用loc属性')
s.loc['沙比']=[77,88,99]
print(s)
print('--------------------------------------添加多行')
d=pd.DataFrame(
    data={'语文':[78,79],'数学':[74,71],'英语':[45,46]},
    index=['小虎','小红']
)
s=pd.concat([s,d])
print(s)
