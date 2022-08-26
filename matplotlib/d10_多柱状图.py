import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_excel('多柱状图.xlsx')
plt.figure('多柱状图',facecolor='y',figsize=(10,7))
x=np.array([1,2,3,4,5,6,7])
y1=df['1月']+df['2月']+df['3月']
y2=df['4月']+df['5月']+df['6月']
y3=df['7月']+df['8月']+df['9月']
y4=df['10月']+df['11月']+df['12月']
plt.xlabel('产品')
plt.ylabel('季度销售量')
w=0.2
for i,j in zip(x, y1):
    plt.text(i,j,j,ha='center',color='g')
for i, j in zip(x, y2):
    plt.text(i+0.2, j, j, ha='center', color='r')
for i, j in zip(x, y3):
    plt.text(i+0.4, j, j, ha='center', color='b')
for i, j in zip(x, y4):
    plt.text(i+0.6, j, j, ha='center', color='y')
plt.rcParams['font.sans-serif']=['SimHei']
plt.bar(x, y1,width=0.2,color='g',alpha=0.5)
plt.bar(x+w, y2,width=0.2,color='r',alpha=0.5)
plt.bar(x+2*w, y3,width=0.2,color='b',alpha=0.5)
plt.bar(x+3*w, y4,width=0.2,color='y',alpha=0.5)
data=df['产品名称']
plt.xticks(x,data)
plt.legend(['第一季度','第二季度','第三季度','第四季度'])
plt.subplots_adjust(left=0.08, right=0.98, bottom=0.09, top=0.95)
plt.show()