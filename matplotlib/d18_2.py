import matplotlib.pyplot as plt
import random
figure,axes=plt.subplots(2,2)#两行两列
# 第一个绘图区
axes[0,0].plot([1,2,3,4,5],[random.randint(1,10) for i in range(5)])
# 第二个绘图区
axes[0,1].scatter([1,2,3,4,5],[random.randint(1,10) for i in range(5)])
# 第三个绘图区
axes[1,0].bar([1,2,3,4,5],[random.randint(1,10) for i in range(5)])
# 第四个绘图区
axes[1,1].pie([random.randint(1,10) for i in range(5)],autopct='%1.1f%%')
plt.show()