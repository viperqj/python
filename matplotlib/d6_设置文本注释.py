import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['KaiTi']
month=[str(i)+'月' for i in range(1,11)]
x=[1,2,3,4,5,6]
y=[10,18,32,47,8,26]
for a,b in zip(x,y):
    plt.text(a,b,b,color='r',ha='center',fontsize='10')
plt.title('测试练习',fontsize='15',color='b')
plt.plot(x,y,marker='o',mfc='w')
plt.annotate('最大数',xy=(4,47),xytext=(5,47),arrowprops={'facecolor':'y','shrink':0.05})
plt.show()
