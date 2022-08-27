import pandas as pd
s=pd.DataFrame(data={
    '原数据':['14-Feb-20','02/14/2020','2020.02.14','2020/02/14','20200214']
})
print(s)
print('--------------------------------------------日期转换')
s1=pd.to_datetime(s['原数据'])
print(s1)
print('要求列索引必须是year,month,day,hour,minute,second------------从多列中组合一个日期')
s2=pd.DataFrame(data={
    'year':[2000,2001,2017,2021],
    'month':[10,2,11,11],
    'day':[9,20,17,17],
    'hour':[5,2,1,0],
    'minute':[1,3,1,4],
    'second':[0,0,0,0]
})
s2['组合后的日期']=pd.to_datetime(s2)
print(s2)



















