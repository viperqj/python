# 只可以读取含有table标签的网页
import pandas as pd
url='http://www.espn.com/nba/salaries'
df=pd.concat(pd.read_html(url,header=0))
print(df)
df.to_csv('demo.csv',index=False)