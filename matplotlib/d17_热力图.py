import matplotlib.pyplot as plt
import pandas as pd
import  random
df=pd.DataFrame(data={
    '姓名':['小明','小红','张三','李四','小虎'],
    '语文':[random.randint(80,150) for i in range(5)],
    '数学':[random.randint(80,150) for i in range(5)],
    '英语':[random.randint(80,150) for i in range(5)]
})
plt.rcParams['font.sans-serif']=['KaiTi']
x=df.loc[:,'语文':]
plt.yticks(range(5),df['姓名'])
plt.xticks(range(3),['语文','数学','英语'])
plt.title('学生成绩热力图')
plt.imshow(x)
plt.colorbar()#显示颜色条
plt.show()
