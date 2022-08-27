import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)
s=pd.DataFrame(data={
    '销量':[4699,1456,8887,4441,666]
},index=['一月','二月','三月','四月','五月'])
print(s)
s['销售差']=s['销量']-s['销量'].shift()
print(s)
















