import matplotlib.pyplot as plt
import random
#绘制第一个子图
plt.subplot(2,2,1)
plt.plot([1,2,3,4,5],[random.randint(1,10) for i in range(5)])
#绘制第一个子图
plt.subplot(2,2,2)
plt.scatter([1,2,3,4,5],[random.randint(1,10) for i in range(5)],color='r')
#绘制第一个子图
plt.subplot(2,1,2)
plt.bar([1,2,3,4,5],[random.randint(1,10) for i in range(5)])
plt.show()