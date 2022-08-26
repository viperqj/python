import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.unicode.east_asian_width', True)
s=pd.DataFrame(data={
    '商品名':['小米手机','华为手机','华为电脑','小米电脑'],
    '销量':[400,200,50,60]
})
plt.rcParams['font.sans-serif']=['KaiTi']
x=s['销量']
labels=s['商品名']
plt.pie(x,labels=labels,autopct='%1.1f%%',labeldistance=1.05,textprops={'fontsize':12})
#保证饼形图为圆形
plt.axis('equal')
plt.legend(labels,fontsize='10')
plt.show()