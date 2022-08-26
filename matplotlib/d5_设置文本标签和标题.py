import matplotlib.pyplot as plt
import random
plt.rcParams['font.sans-serif']=['KaiTi']
month=[str(i)+'月' for i in range(1,11)]
x=[i for i in range(1,11)]
y=[random.randint(1,10) for i in range(10)]#包含10
plt.xticks(range(1,11),month)
plt.yticks(range(1,11))
for a,b in zip(x,y):
    plt.text(a,b,(a,b),color='r',ha='center',fontsize='10')
plt.title('测试练习',fontsize='15',color='b')
plt.plot(x,y,marker='o',mfc='w')
plt.legend(('销售次数',))
plt.show()