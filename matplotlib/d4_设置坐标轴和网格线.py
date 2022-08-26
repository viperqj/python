#  设置坐标轴标题
#
# import matplotlib.pyplot as plt
# import pandas as pd
# plt.figure(num='温度',figsize=(10,4),facecolor='y')
# s=pd.date_range(start='2022-08-02',freq='D',periods=10)
# df=pd.DataFrame(data=[30,29,33,38,28,26,31,24,19,25],index=s,columns=['温度'])
# x=s
# y=df['温度']
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.title('天气预报')
# plt.xlabel('日期')
# plt.ylabel('温度')
# plt.plot(x,y,marker='o',mfc='w')
# plt.show()

# 设置坐标轴刻度
# import matplotlib.pyplot as plt
# import random
# plt.rcParams['font.sans-serif']=['KaiTi']
# month=[str(i)+'月' for i in range(1,11)]
# x=[i for i in range(1,11)]
# y=[random.randint(1,10) for i in range(10)]#包含10
# plt.xticks(range(1,11),month)
# plt.yticks(range(1,11))
# plt.plot(x,y,marker='o')
# plt.show()


#设置坐标轴范围
# import matplotlib.pyplot as plt
# import random
# plt.rcParams['font.sans-serif']=['KaiTi']
# month=[str(i)+'月' for i in range(1,11)]
# x=[i for i in range(1,11)]
# y=[random.randint(1,10) for i in range(10)]#包含10
# plt.xticks(range(1,11),month)
# plt.yticks(range(1,11))
# plt.xlim(1,20)
# plt.ylim(1,20)
# plt.plot(x,y,marker='o')
# plt.show()


# 设置网格线
import matplotlib.pyplot as plt
import random
plt.rcParams['font.sans-serif']=['KaiTi']
month=[str(i)+'月' for i in range(1,11)]
x=[i for i in range(1,11)]
y=[random.randint(1,10) for i in range(10)]#包含10
plt.xticks(range(1,11),month)
plt.yticks(range(1,11))
plt.plot(x,y,marker='o')
plt.grid(color='0.5',linestyle='--',linewidth='1',axis='both')#x y both
plt.show()







