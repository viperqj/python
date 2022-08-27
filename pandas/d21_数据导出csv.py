import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
s1=pd.DataFrame(data={
    '学号':['1001','1002','1003'],
    '语文':[56.12,38.36,47.89],
    '数学':[88,19,70],
    '英语':[96,78,81]
})
print(s1)
s1.to_csv('数据导出.csv',index=False,columns=['学号','语文','数学','英语'],float_format='%.1f')