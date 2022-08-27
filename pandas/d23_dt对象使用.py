import pandas as pd
s=pd.DataFrame(data={
    '原数据':['1999.02.12','2003.03.30','2020.02.14','2020.10.25','1949.10.01']
})
print(s)
s['日期']=pd.to_datetime(s['原数据'])
s['年']=s['日期'].dt.year
s['月']=s['日期'].dt.month
s['日']=s['日期'].dt.day
s['星期']=s['日期'].dt.day_name()
s['季度']=s['日期'].dt.quarter
print(s)
