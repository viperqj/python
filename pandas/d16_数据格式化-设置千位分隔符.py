import pandas as pd
s=pd.DataFrame(data={
    'name':['电脑','汽车','手机'],
    '价格':[18888,888888,8888]
})
print(s)
s['价格']=s['价格'].apply(lambda x:format(int(x),','))
print(s)