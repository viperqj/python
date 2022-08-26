import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['KaiTi']
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'out'
month=[str(i)+'月' for i in range(1,11)]
x=[1,2,3,4,5,6]
y=[10,18,32,47,8,26]
plt.plot(x,y)
for a,b in zip(x,y):
    plt.text(a,b,b,color='r',ha='center',fontsize='10')
plt.title('测试练习',fontsize='15',color='b')
plt.tick_params(bottom=True,left=True,right=True,top=True)
plt.annotate('最大数',xy=(4,47),xytext=(5,47),arrowprops={'facecolor':'y','shrink':0.05})
plt.subplots_adjust(left=0.1,right=0.9,bottom=0.09,top=0.9)
plt.show()
