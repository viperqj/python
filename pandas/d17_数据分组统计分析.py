import pandas as pd
s=pd.DataFrame(data={
    '产品名称':['电脑','手机','键盘','鼠标','手机','键盘','鼠标','电脑'],
    '成交额':[4100,1000,100,100,800,200,50,3000],
    '成交量':[10,30,45,60,10,70,80,20]
    })
print(s)
print('-------------------------------------------------------------groupby()')
print('---------------------------------按照一列进行分组')
print(s.groupby('产品名称',as_index=False).sum())#对量和价都进行求和统计
print('---------------------------------按照多列进行分组')
s1=pd.DataFrame(data={
    '产品名称':['电脑','手机','键盘','鼠标','手机','键盘','鼠标','电脑'],
    '销售员':['张三','李四','张三','王五','李四','王五','王五','李四'],
    '成交额':[4100,1000,100,100,800,200,50,3000],
    '成交量':[10,30,45,60,10,70,80,20]
    })
print(s1,'\n')
print(s1.groupby(['产品名称','销售员'],as_index=False).sum())
print('---------------------------------分组对指定列列进行计算')
print(s.groupby('产品名称',as_index=False,sort=False)['成交量'].sum())








