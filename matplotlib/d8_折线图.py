import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('tw.csv')
for i in range(0,909):
    for j in range(0,1):
       df.iloc[i,j]=str(df.iloc[i,j])
df['dateId']=pd.to_datetime(df['dateId'])
df=df.set_index('dateId')
df=df.resample('Q').sum().to_period('Q')
plt.figure('简单折线图',figsize=(8,6),facecolor='y',)
x=['2020Q1','2020Q2','2020Q3','2020Q4','2021Q1','2021Q2','2021Q3','2021Q4','2022Q1','2022Q2', '2022Q3']
y=list(df['confirmedIncr'])
plt.plot(x, y, color='b', linestyle='-', marker='o', mfc='w')
plt.xlabel('季度')
plt.ylabel('新增数量')
for a,b in zip(x,y):
        plt.text(a,b,b,color='r',ha='center',fontsize='10')
plt.title('台湾疫情新增趋势按季度')
plt.rcParams['font.sans-serif']=['SimHei']
plt.grid(color='0.5',linestyle='--',linewidth='1',axis='both')
plt.subplots_adjust(left=0.1,right=0.9,bottom=0.09,top=0.9)
plt.show()