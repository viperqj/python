import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
print('-------------------------------------------------多对一')
s1=pd.DataFrame(data={
    '学号':[1001,1002,1003],
    '语文':[56,38,47],
    '数学':[88,19,70],
    '英语':[96,78,81]
})
s2=pd.DataFrame(data={
    '学号':[1004,1005,1006],
    '语文':[77,98,41],
    '数学':[65,26,41],
    '英语':[99,89,28]
})
new_s=pd.concat([s1,s2],keys=['表1','表2'])
print(new_s)
print('-------------------------------------------------纵向合并')
new_s=pd.concat([s1,s2],ignore_index=True)
print(new_s)
print('-------------------------------------------------横向向合并')
s1=pd.DataFrame(data={
    'A':['1001','1002','1003'],
    'B':['56','38','47'],
    'C':['88','19','70'],
    'D':['96','78','81']
})
s2=pd.DataFrame(data={
    'D':['a','b','e','f'],
    'E':['c','d','h','j']
})
new_s=pd.concat([s1,s2],axis=1)
print(new_s)
print('-------------------------------------------------交叉合并')
s1=pd.DataFrame(data={
    'A':['1001','1002','1003'],
    'B':['56','38','47'],
    'C':['88','19','70'],
    'D':['a','b','e']
})
s2=pd.DataFrame(data={
    'D':['a','b','e','f'],
    'E':['c','d','h','j']
})
new_s=pd.concat([s1,s2],axis=1,join='inner')
print(new_s)










