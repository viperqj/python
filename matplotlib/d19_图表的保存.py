import matplotlib.pyplot as plt
import random
fig=plt.figure()
#绘制第一个子图
ax1=fig.add_subplot(2,2,1)
ax1.plot([1,2,3,4,5],[random.randint(1,10) for i in range(5)])
#绘制第二个子图
ax2=fig.add_subplot(2,2,2)
ax2.scatter([1,2,3,4,5],[random.randint(1,10) for i in range(5)],color='r')
#绘制第三个子图
ax3=fig.add_subplot(2,2,3)
ax3.bar([1,2,3,4,5],[random.randint(1,10) for i in range(5)])
# 绘制第四个
ax4=fig.add_subplot(2,2,4)
ax4.pie([random.randint(1,10) for i in range(5)],autopct='%1.1f%%')
plt.savefig('demo.png')
plt.show()