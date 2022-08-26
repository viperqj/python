import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame(data={
    '总成绩':[61,71,89,74,36,25,86,73,84,86,87]
})
plt.rcParams['font.sans-serif']=['KaiTi']
x=df['总成绩']
plt.xlabel('分数')
plt.ylabel('人数')
plt.title('直方图')
bins=[0,10,20,30,40,50,60,70,80,90,100]
plt.xticks(bins)
plt.hist(x,bins,facecolor='g',edgecolor='k')
plt.show()