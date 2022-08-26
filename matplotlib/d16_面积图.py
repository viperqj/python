import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel('多柱状图.xlsx')
plt.rcParams['font.sans-serif']=['KaiTi']
x=df['产品名称']
y1=df['1月']+df['2月']+df['3月']
y2=df['4月']+df['5月']+df['6月']
y3=df['7月']+df['8月']+df['9月']
y4=df['10月']+df['11月']+df['12月']
plt.stackplot(x,y1,y2,y3,y4)
plt.legend(['第一季度','第二季度','第三季度','第四季度'])
plt.show()